# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal portfolio + learning-notes site built with Hugo on the HugoBlox "dev-portfolio" template (Tailwind CSS v4, Pagefind search). Nearly all work here is editing Markdown/YAML content. There is no custom theme code and no `layouts/` directory. Templates come from HugoBlox Hugo Modules (see `go.mod` and `config/_default/module.yaml`) and are not vendored.

For questions about HugoBlox (block types, front matter, config options, docs layout, upgrades) or for theme/build issues, consult the HugoBlox documentation: https://hugoblox.com/docs.

## Commands

```bash
pnpm install          # install Tailwind CLI + Pagefind (required by Hugo >= 0.161)
pnpm dev              # hugo server --disableFastRender (local preview)
pnpm build            # hugo --minify && pagefind --site public
```

`pnpm check:docs` (`scripts/check_doc_conventions.py`) checks `content/doc/` against the naming and capitalization conventions below. Add `--fix` to rewrite capitalization in place; file and folder names are only reported, never renamed. It runs automatically:

- after every Claude `Write`/`Edit` under `content/doc/` (PostToolUse hook in `.claude/settings.json`); violations are fed back to Claude to fix.
- on `git commit` (`.githooks/pre-commit`, enabled once per clone with `git config core.hooksPath .githooks`): staged doc files are checked, capitalization is fixed in the working tree, and the commit is blocked until the fixes are reviewed and staged.

Terms that should keep their own casing in titles (key names, lowercase product names) go in `scripts/title-case-allowlist.txt`.

There are no other tests or linters. To check a change, run `hugo` (or `pnpm build`) and confirm it finishes without errors. `public/`, `resources/` and `hugo_stats.json` are build output and are gitignored.

## Deployment

- The site is deployed on **Netlify**, which is connected to the GitHub repo. Every push to `main` triggers a Netlify production deploy, so a push publishes the site. `netlify.toml` defines the build command (`pnpm install`, `hugo --gc --minify`, Pagefind), the deploy-preview and branch-deploy variants, and the pinned `HUGO_VERSION` (0.165.0, which matches the local Hugo 0.165 extended). When the Hugo version changes, update it here.
- The GitHub Actions workflows (`build.yml` and `deploy.yml`) are leftovers from the HugoBlox template. They are not the deploy path. They read `build.hugo_version` and `deploy.host` from `hugoblox.yaml`.
- The `upgrade.yml` workflow (manual only) bumps HugoBlox modules through `pnpm dlx hugoblox@latest upgrade` and opens a PR.

## Content layout

- `content/_index.md`: the landing page, built from a list of HugoBlox `sections` (`block: dev-hero`, `resume-experience`, `awards`, `tech-stack`, etc.). Blocks that are commented out are disabled on purpose.
- `data/authors/me.yaml` and `data/authors/awards.yaml`: author profile, experience and awards data that the landing-page blocks render. Avatar images are in `assets/media/authors/`. The main image was renamed (`me_1.jpg`) on purpose so the avatar does not show on the landing page.
- `config/_default/params.yaml`: site branding and features (math, TOC, etc.). `hugo.yaml` holds the core Hugo config, and `menus.yaml` holds the nav.
- `content/blog`, `content/projects`, `content/publications`, `content/recommendations`: page bundles (`<slug>/index.md` plus their assets).

### `content/doc/`: learning notes (the most active area)

- `content/doc/_index.md` sets `type: docs` and cascades it, so everything below uses the HugoBlox docs layout with a sidebar.
- Hierarchy: `doc/<topic>/<course>/<NN-module>/<lesson>.md`. Examples: `doc/claude/claude-code-101/02-daily-workflows/context_management.md`, and `doc/algo/` for algorithms.
- Each folder has an `_index.md` with `title`, optional `linkTitle`, `date` and `weight`. Lesson files use `title`, `date` and `weight`.
- **Sidebar order is set by `weight`.** The convention is steps of 100 (100, 200, 300, …) for modules and lessons, and module folders also carry a `NN-` prefix.
- A course `_index.md` links to the course source and has a "Course Outline" list of relative links to its module folders.
- Do **not** add `sidebar: open: true` to `_index.md`. It was removed on purpose so that sections stay collapsed except for the current page's ancestors.
- Images are hosted externally on `https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/...` (uploaded with uPic) and referenced with absolute URLs, not stored in the repo.
- Notes are summaries of course lessons: headings, bullet points, bold for key terms, and tables for comparisons such as commands.
- Naming and capitalization conventions:

    - @.claude/conventions/doc-naming.md
    - @.claude/conventions/doc-capitalization.md

## Commit style

Short imperative or past-tense subject lines that describe the content change, for example `Summarize claude-code-101 "daily workflows".`
