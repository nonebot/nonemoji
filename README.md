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

### 快速提交

使用如下命令，选择一个 emoji 并填写提交信息：

```bash
nonemoji commit
```

### 交互式使用

```bash
nonemoji
```
