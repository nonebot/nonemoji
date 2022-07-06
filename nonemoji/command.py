import shlex
import subprocess
from pathlib import Path
from typing import List, Optional

from .emoji import EMOJIS
from .feature import prompt


def handle_hook(commit_msg_file: str, **_):
    file = Path(commit_msg_file)
    original_msg = file.read_text()
    new_msg = prompt(original_msg)
    file.write_text(new_msg)


def handle_commit(
    emoji: Optional[str] = None,
    message: Optional[str] = None,
    args: Optional[List[str]] = None,
    **_,
):
    args = args or []
    new_msg = prompt(message, emoji=emoji)
    pargs = ["git", "commit", "-m", new_msg, *args]
    try:
        subprocess.run(pargs, check=True)
    except Exception as e:
        print("Oops! An error ocurred while committing: ", e)
        print("You can run the same commit with this command:")
        print(f"\t{' '.join(shlex.quote(arg) for arg in pargs)}")


def handle_list(**_):
    text = "\n".join(emoji.to_string() for emoji in EMOJIS.values())
    print(text)
