# 🐙 Git & GitHub

Notes and workflows for Git version control and GitHub.

## 📋 Topics Covered

| Topic | Status |
|-------|--------|
| Git Setup & Configuration | ✅ Done |
| init, add, commit | ✅ Done |
| Branching & Merging | 🟡 In Progress |
| Remote Repositories (push, pull, fetch) | 🟡 In Progress |
| Pull Requests & Code Review | 🔴 Upcoming |
| GitHub Issues | 🔴 Upcoming |
| GitHub Actions (CI/CD) | 🔴 Upcoming |
| Git Stash & Tags | 🔴 Upcoming |
| Resolving Merge Conflicts | 🔴 Upcoming |

## 💡 My Git Workflow

```bash
# Start of every session
git status
git pull

# After making changes
git add .
git commit -m "feat: descriptive message"
git push
```

## 📝 Commit Message Convention

I follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — new feature or content
- `fix:` — bug fix
- `docs:` — documentation change
- `chore:` — maintenance, tooling
- `refactor:` — code restructuring

> See also: [CHEATSHEETS.md](../../CHEATSHEETS.md) for Git command reference
