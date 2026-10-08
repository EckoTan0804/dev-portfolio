# Naming Conventions for `content/doc/`

## Folders: kebab-case

- Lowercase, words joined by `-`. Apostrophes are dropped (`expanding-claudes-reach`).
- Topic and course folders have no prefix: `algo`, `claude`, `claude-code-101`, `best-practice`.
- Module folders are named `NN-<name>`, with a two-digit number counting up from `00`: `00-meet-claude`, `02-expanding-claudes-reach`. The name usually follows the module's title.

## Files: snake_case

- A lesson file is named after its title in snake_case (`<title_in_snake_case>.md`): all lowercase, words joined by `_`, and punctuation (`'`, `:`, `→`, `.`) dropped.
  - "Plugins: Encode Your Team's Expertise" → `plugins_encode_your_teams_expertise.md`
  - "A CLAUDE.md That Follows" → `a_claude_md_that_follows.md`
  - "The Explore → Plan → Code → Commit Workflow" → `the_explore_plan_code_commit_workflow.md`
- Lesson files have **no number prefix**. Their order comes from `weight`.
- Every folder's section page is named `_index.md`.

## Notes

- Hugo builds URLs from these names, so lesson URLs contain underscores and folder URLs use hyphens. Renaming a file or folder changes its URL, so when you rename one, update every link to it.
