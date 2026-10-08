---
title: "Verification Skills"
date: 2026-10-03
weight: 200
---

> [!NOTE]
>
> ### TL;DR
>
> - A skill is a folder with a SKILL.md inside it: a name, a description that triggers it, and the procedure itself.
> - **If you've typed the same multi-step instruction twice, that's a skill.**

The rule of thumb: **If you've typed the same multi-step instruction twice, that's a skill.**

## Skill Folder

A skill isn't just a single `SKILL.md` file. The folder around it can carry other things.

- Drop a `reference.md` next to `SKILL.md` for detailed material, then link to it from `SKILL.md`. Claude reads it only when it needs that depth. Your main file stays short.

- Put scripts in the folder too. Claude executes them rather than loading their contents into context. That means a skill can carry its own tooling, like a `check.sh` that runs all the gates.

> [!TIP]
> keep SKILL.md itself **lean**. Push the heavy material (the long explanations and the executable scripts) into side files. 
>
> The lean file describes what to do. The side files hold the depth and the tools.

## Which Instruction Surface Owns Which Rule

![instruction surface](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2026-10-07%2011.00.14.png)



|                  | Owns                                                         |
| ---------------- | ------------------------------------------------------------ |
| `CLAUDE.md` file | Conventions that apply all the time, things like naming rules or where files go. |
| Skill            | Procedures and reference material tied to a particular kind of task belong in a skill. |
| Hook             | A rule that Claude **must not** be able to skip.             |

 

