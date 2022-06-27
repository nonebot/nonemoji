import re
from typing import List, Match, Optional

from wcwidth import wcswidth
from prompt_toolkit.styles import Style
from noneprompt import Choice, ListPrompt

from .emoji import emojis

MESSAGE_REGEX = re.compile(r"^:(?P<emoji>\w+):(?P<message>[\s\S]+)$")


def validate(message: str) -> Optional[Match[str]]:
    return MESSAGE_REGEX.match(message)


def main():
    default_style = Style.from_dict(
        {
            "questionmark": "fg:#673AB7 bold",
            "question": "",
            "sign": "",
            "unsign": "",
            "selected": "",
            "pointer": "bold",
            "annotation": "",
            "answer": "bold",
        }
    )

    src_choices: List[Choice[str]] = [
        Choice(
            f"{emoji.emoji}{' '*(4-wcswidth(emoji.emoji))}- {emoji.description}",
            emoji.name,
        )
        for emoji in emojis
    ]
    result = ListPrompt("Where to store the plugin?", src_choices).prompt(
        style=default_style
    )
