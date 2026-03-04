# 🔄 CI/CD

Notes on Continuous Integration and Continuous Deployment.

## 📋 Topics to Cover

| Topic | Status |
|-------|--------|
| What is CI/CD? | 🔴 Planned |
| GitHub Actions Basics | 🔴 Planned |
| Writing a Workflow YAML file | 🔴 Planned |
| Running Tests in CI | 🔴 Planned |
| Automatic Deployment | 🔴 Planned |
| Secrets & Environment Variables in Actions | 🔴 Planned |
| Deploy to GitHub Pages via Actions | 🔴 Planned |

## 💡 GitHub Actions Quick Start

```yaml
# .github/workflows/main.yml
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run a script
        run: echo "Hello from CI!"
```

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Skills: Hello GitHub Actions](https://github.com/skills/hello-github-actions)
