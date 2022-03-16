from .prompts import ListPrompt
from .prompts import Choice
from .prompts import Style
from typing import List
from .emoji import emojis
from wcwidth import wcswidth


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
            f"{emoji.emoji}{' '*(4-wcswidth(emoji.emoji))}- {emoji.description}", emoji.name
        )
        for emoji in emojis
    ]
    print(
        ListPrompt("Where to store the plugin?", src_choices)
        .prompt(style=default_style)
        .data
    )