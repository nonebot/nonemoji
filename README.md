# Nonemoji

自维护的 gitmoji-cli，删减了部分 emoji

## 安装

```bash
poetry add nonemoji --dev
```

## 在 pre-commit 中使用

```yaml
# .pre-commit-config.yaml
default_install_hook_types: [pre-commit, prepare-commit-msg]
repos:
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        stages: [commit]

  - repo: https://github.com/psf/black
    rev: 22.6.0
    hooks:
      - id: black
        stages: [commit]

  - repo: https://github.com/nonebot/nonemoji
    rev: v0.1.3
    hooks:
      - id: nonemoji
        stages: [pre-commit-msg]
```

## 使用

commit时使用`nonemoji`命令:

```sh
$ nonemoji

[?] What do you want to do? (Use ↑ and ↓ to choose, Enter to submit)
❯ Start to commit changes
  List all available emojis
  Search for an emoji

// 选择 Start to commit changes

[?] Choose a gitmoji: (Use ↑ and ↓ to choose, Enter to submit)
❯ ✨  - Introduce new features.
  🐛  - Fix a bug.
  📝  - Add or update documentation.
  📄  - Add or update license.
  🎨  - Improve structure / format of the code.
  ♻️   - Refactor code.
  ✅  - Add, update, or pass tests.

// 选择 🐛  - Fix a bug.

[?] Choose a gitmoji: 🐛  - Fix a bug.
[?] Enter the commit title: <你输入的内容>

//...自动运行 git commit -m ":bug: <你输入的内容>"

```
