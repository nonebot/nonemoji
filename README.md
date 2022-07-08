# Nonemoji

自维护的 gitmoji-cli，删减了部分 emoji

## 安装

```bash
poetry add nonemoji --dev
```

## pre-commit 使用

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
    rev: v0.1.1
    hooks:
      - id: nonemoji
```
