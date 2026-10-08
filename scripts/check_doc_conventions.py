#!/usr/bin/env python3
"""Check content/doc/ against .claude/conventions/doc-naming.md and doc-capitalization.md.

Usage:
  check_doc_conventions.py                 check every file under content/doc/
  check_doc_conventions.py PATH...         check these files and their ancestor folders
  check_doc_conventions.py --fix [PATH...] also rewrite capitalization violations in place
  check_doc_conventions.py --hook          Claude Code PostToolUse hook (reads JSON on stdin)

Exit codes: 0 clean, 1 violations (or fixes applied), 2 violations in --hook mode.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "content" / "doc"
ALLOWLIST_FILE = Path(__file__).resolve().parent / "title-case-allowlist.txt"

# Paths (relative to content/doc) exempt from the file-naming checks.
NAMING_EXCEPTIONS = set()

# Minor words that are always lowercase mid-title; flagged when capitalized.
STRICT_MINOR = {
    "a", "an", "the",
    "and", "but", "or", "nor", "for", "so", "yet",
    "to", "as",
    "of", "with", "from", "at", "by", "into", "onto", "via", "vs", "per",
}
# Prepositions that may also be verb particles or subordinating conjunctions
# ("Set Up", "Before You Start"): allowed lowercase, not flagged when capitalized.
AMBIGUOUS_MINOR = {
    "about", "above", "across", "after", "against", "along", "among", "around",
    "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond",
    "despite", "down", "during", "except", "in", "inside", "like", "near", "off",
    "on", "out", "outside", "over", "past", "since", "through", "throughout", "till",
    "toward", "towards", "under", "underneath", "until", "up", "upon", "within",
    "without", "amid", "versus",
}
MINOR = STRICT_MINOR | AMBIGUOUS_MINOR

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SNAKE_FILE = re.compile(r"^[a-z0-9]+(_[a-z0-9]+)*\.md$")
MODULE = re.compile(r"^(\d{2})-")
NUMBER_PREFIX = re.compile(r"^\d+[_-]")
FRONT_TITLE = re.compile(r"^(title|linkTitle):[ \t]*(.*?)[ \t]*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def load_allowlist():
    try:
        lines = ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    return [l.strip() for l in lines if l.strip() and not l.lstrip().startswith("#")]


ALLOWLIST = load_allowlist()


def snake(title):
    s = re.sub(r"['’]", "", title.lower())
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def mask(text):
    """Blank out spans that title case doesn't apply to, keeping offsets."""
    def blank(m):
        return "\x00" * len(m.group(0))
    text = re.sub(r"`[^`]*`", blank, text)
    text = re.sub(r"\]\([^)]*\)", blank, text)
    text = re.sub(r"\{#[^}]*\}", blank, text)
    for term in ALLOWLIST:
        text = re.sub(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", blank, text)
    return text


def title_case_issues(text):
    """Return a list of (offset, word, 'upper'|'lower') for words with the wrong case."""
    masked = mask(text)
    # Masked spans (code, allowlisted terms) still occupy a word position.
    words = []  # (offset, word or None, hyphen_tail, after_colon)
    prev_chunk = ""
    for chunk in re.finditer(r"\S+", masked):
        after_colon = prev_chunk.endswith(":")
        first_in_chunk = True
        if chunk.group(0).strip("\x00") == "" or chunk.group(0).startswith("\x00"):
            words.append((chunk.start(), None, False, False))
            first_in_chunk = False
        for part in re.finditer(r"[^-/–\x00]+", chunk.group(0)):
            m = re.match(r"[(\[{\"'*_~“‘]*([A-Za-z][A-Za-z0-9'’.]*)", part.group(0))
            if m:
                offset = chunk.start() + part.start() + m.start(1)
                tail = part.start() > 0 and chunk.group(0)[part.start() - 1] == "-"
                words.append((offset, m.group(1), tail, after_colon and first_in_chunk))
                first_in_chunk = False
        if re.search(r"[A-Za-z\x00]", chunk.group(0)):
            prev_chunk = chunk.group(0)

    issues = []
    for i, (offset, word, tail, after_colon) in enumerate(words):
        if word is None:
            continue
        key = word.lower().rstrip(".")
        cap = word[0].isupper()
        if not cap and any(c.isupper() for c in word[1:]):
            continue  # brand spelling such as iPhone or macOS
        forced = i == 0 or i == len(words) - 1 or after_colon or (tail and key not in STRICT_MINOR)
        if forced:
            if not cap:
                issues.append((offset, word, "upper"))
        elif key in MINOR:
            if cap and key in STRICT_MINOR and not word[1:].isupper():
                issues.append((offset, word, "lower"))
        elif not cap:
            issues.append((offset, word, "upper"))
    return issues


def apply_case(text, issues):
    chars = list(text)
    for offset, _, case in issues:
        chars[offset] = chars[offset].upper() if case == "upper" else chars[offset].lower()
    return "".join(chars)


def describe(kind, value, issues):
    parts = [f'"{w}" should be {"capitalized" if c == "upper" else "lowercase"}' for _, w, c in issues]
    return f'{kind} "{value}": ' + "; ".join(parts)


def rel(path):
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


class Checker:
    def __init__(self, fix=False):
        self.fix = fix
        self.violations = []
        self.fixes = []
        self.seen_dirs = set()

    def report(self, path, line, msg):
        loc = f"{rel(path)}:{line}" if line else rel(path)
        self.violations.append(f"{loc}: {msg}")

    def check_dir(self, d):
        if d in self.seen_dirs or d == DOC:
            return
        self.seen_dirs.add(d)
        parts = d.relative_to(DOC).parts
        if not KEBAB.match(d.name):
            self.report(d, 0, f'folder name "{d.name}" should be kebab-case')
        if len(parts) == 3 and not MODULE.match(d.name):
            self.report(d, 0, f'module folder "{d.name}" should start with a two-digit "NN-" prefix')
        if not (d / "_index.md").is_file():
            self.report(d, 0, "folder has no _index.md")
        if len(parts) == 2:
            seen = {}
            for sub in sorted(p for p in d.iterdir() if p.is_dir()):
                m = MODULE.match(sub.name)
                if m:
                    if m.group(1) in seen:
                        self.report(sub, 0, f'duplicate module number "{m.group(1)}" (also {seen[m.group(1)]})')
                    seen.setdefault(m.group(1), sub.name)

    def check_file(self, path):
        for parent in path.relative_to(DOC).parents:
            if parent != Path("."):
                self.check_dir(DOC / parent)

        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        changed = False
        title = None

        # Front matter
        end = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    end = i
                    break
        for i in range(1, end):
            m = FRONT_TITLE.match(lines[i])
            if not m:
                continue
            raw, start = m.group(2), m.start(2)
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
                raw, start = raw[1:-1], start + 1
            if m.group(1) == "title":
                title = raw
            issues = title_case_issues(raw)
            if issues:
                changed |= self.handle(path, lines, i, start, raw, m.group(1), issues)

        # ## headings outside fenced code
        in_fence = False
        for i in range(end + 1 if end else 0, len(lines)):
            if FENCE.match(lines[i]):
                in_fence = not in_fence
                continue
            if in_fence or not lines[i].startswith("## "):
                continue
            raw = lines[i][3:].rstrip()
            issues = title_case_issues(raw)
            if issues:
                changed |= self.handle(path, lines, i, 3, raw, "heading", issues)

        if changed:
            path.write_text("\n".join(lines), encoding="utf-8")

        # File naming
        relpath = path.relative_to(DOC).as_posix()
        if path.name == "_index.md" or relpath in NAMING_EXCEPTIONS:
            return
        if NUMBER_PREFIX.match(path.name):
            self.report(path, 0, f'lesson file "{path.name}" should have no number prefix (order comes from weight)')
        elif not SNAKE_FILE.match(path.name):
            self.report(path, 0, f'lesson file "{path.name}" should be snake_case')
        if title is None:
            self.report(path, 0, "no title in front matter")
        elif snake(title) + ".md" != path.name:
            self.report(path, 0, f'file name should be "{snake(title)}.md" to match title "{title}"')

    def handle(self, path, lines, i, start, raw, kind, issues):
        if not self.fix:
            self.report(path, i + 1, describe(kind, raw, issues))
            return False
        fixed = apply_case(raw, issues)
        lines[i] = lines[i][:start] + fixed + lines[i][start + len(raw):]
        self.fixes.append(f'{rel(path)}:{i + 1}: {kind} "{raw}" -> "{fixed}"')
        return True


def doc_markdown(path):
    """Return the resolved path if it is a Markdown file under content/doc, else None."""
    p = Path(path)
    p = (p if p.is_absolute() else ROOT / p).resolve()
    if p.suffix != ".md" or not p.is_file():
        return None
    try:
        p.relative_to(DOC)
    except ValueError:
        return None
    return p


def main(argv):
    hook = "--hook" in argv
    fix = "--fix" in argv and not hook
    args = [a for a in argv if not a.startswith("--")]

    if hook:
        try:
            data = json.load(sys.stdin)
        except ValueError:
            return 0
        file_path = (data.get("tool_input") or {}).get("file_path")
        files = [p for p in [doc_markdown(file_path)] if p] if file_path else []
        if not files:
            return 0
    elif args:
        files = [p for p in map(doc_markdown, args) if p]
    else:
        files = sorted(DOC.rglob("*.md"))

    checker = Checker(fix=fix)
    if not args and not hook:
        for d in sorted(p for p in DOC.rglob("*") if p.is_dir()):
            checker.check_dir(d)
    for f in files:
        checker.check_file(f)

    for line in checker.fixes:
        print(f"fixed {line}")
    if hook:
        if checker.violations:
            print("content/doc convention violations (see .claude/conventions/):", file=sys.stderr)
            for v in checker.violations:
                print("  " + v, file=sys.stderr)
            return 2
        return 0
    for v in checker.violations:
        print(v)
    return 1 if checker.violations or checker.fixes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
