from pathlib import Path

from .feature import prompt


def handle_hook(commit_msg_file: str, **_):
    file = Path(commit_msg_file)
    original_msg = file.read_text()
    new_msg = prompt(original_msg)
    file.write_text(new_msg)


def handle_commit(message: str, **_):
    new_msg = prompt(message)
    # TODO: call git commit
