# 📋 Cheatsheets

Quick reference cards for the tools I use every day. Bookmark this! 🔖

---

## 🐙 Git Commands Cheatsheet

### Setup
| Command | Description |
|---------|-------------|
| `git config --global user.name "Name"` | Set your global username |
| `git config --global user.email "email"` | Set your global email |
| `git config --list` | View all configuration settings |

### Starting a Repository
| Command | Description |
|---------|-------------|
| `git init` | Initialize a new local Git repository |
| `git clone <url>` | Clone a remote repository to your machine |

### Making Changes
| Command | Description |
|---------|-------------|
| `git status` | Check status of working directory |
| `git add <file>` | Stage a specific file for commit |
| `git add .` | Stage all changes in current directory |
| `git commit -m "message"` | Commit staged changes with a message |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |

### Branching
| Command | Description |
|---------|-------------|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch |
| `git checkout <name>` | Switch to a branch |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git merge <branch>` | Merge a branch into current branch |
| `git branch -d <name>` | Delete a local branch |

### Remote Repositories
| Command | Description |
|---------|-------------|
| `git remote -v` | View remote connections |
| `git remote add origin <url>` | Add a remote repository |
| `git push origin <branch>` | Push branch to remote |
| `git pull` | Fetch and merge latest remote changes |
| `git fetch` | Fetch changes without merging |

### Undoing Changes
| Command | Description |
|---------|-------------|
| `git restore <file>` | Discard changes in working directory |
| `git restore --staged <file>` | Unstage a staged file |
| `git revert <commit>` | Create a new commit that undoes changes |
| `git log --oneline` | View compact commit history |

---

## 🐧 Linux Terminal Commands Cheatsheet

### Navigation
| Command | Description |
|---------|-------------|
| `pwd` | Print current working directory |
| `ls` | List files in current directory |
| `ls -la` | List all files with details (including hidden) |
| `cd <dir>` | Change directory |
| `cd ..` | Go up one directory |
| `cd ~` | Go to home directory |

### File Operations
| Command | Description |
|---------|-------------|
| `touch <file>` | Create a new empty file |
| `mkdir <dir>` | Create a new directory |
| `mkdir -p a/b/c` | Create nested directories |
| `cp <src> <dest>` | Copy a file |
| `mv <src> <dest>` | Move or rename a file |
| `rm <file>` | Remove a file |
| `rm -rf <dir>` | Remove a directory recursively (careful!) |

### Viewing Files
| Command | Description |
|---------|-------------|
| `cat <file>` | Display file contents |
| `less <file>` | View file with pagination |
| `head <file>` | Show first 10 lines |
| `tail <file>` | Show last 10 lines |
| `grep "text" <file>` | Search for text in a file |

### System Info
| Command | Description |
|---------|-------------|
| `whoami` | Show current user |
| `uname -a` | Show system information |
| `df -h` | Show disk usage |
| `free -h` | Show memory usage |
| `top` | Show running processes |
| `ps aux` | List all running processes |

### Permissions
| Command | Description |
|---------|-------------|
| `chmod +x <file>` | Make a file executable |
| `chmod 755 <file>` | Set read/write/execute permissions |
| `sudo <command>` | Run command as superuser |

---

## ✍️ Markdown Syntax Cheatsheet

### Text Formatting
| Syntax | Result |
|--------|--------|
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `` `inline code` `` | `inline code` |

### Headings
```markdown
# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
```

### Lists
```markdown
- Unordered item 1
- Unordered item 2
  - Nested item

1. Ordered item 1
2. Ordered item 2

- [x] Completed task
- [ ] Pending task
```

### Links & Images
```markdown
[Link text](https://url.com)
![Alt text](image-url.jpg)
```

### Code Blocks
````markdown
```python
print("Hello, World!")
```
````

### Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Blockquotes
```markdown
> This is a blockquote
```

### Horizontal Rule
```markdown
---
```

---

*Last Updated: 2024-01-20*
