import re
import contextlib
from dataclasses import dataclass
from typing import Optional, cast

from wcwidth import wcswidth
from noneprompt import Choice, ListPrompt, InputPrompt

from .emoji import EMOJIS, Emoji

MESSAGE_REGEX = re.compile(r"^:(?P<emoji>\w+):(?P<message>[\s\S]+)$")


@dataclass
class Message:
    emoji: Optional[Emoji] = None
    content: Optional[str] = None

    @property
    def valid(self) -> bool:
        return bool(self.emoji and self.content)

    def to_string(self) -> str:
        if not self.valid:
            raise ValueError("Message is not valid")
        emoji = cast(Emoji, self.emoji)
        content = cast(str, self.content)
        return f"{emoji.code} {content.strip()}"


def transform(message: str) -> Message:
    match = MESSAGE_REGEX.match(message)
    if match:
        return Message(EMOJIS.get(match.group("emoji")), match.group("message"))
    return Message(None, message)


def prompt(original_msg: Optional[str] = None, emoji: Optional[str] = None) -> str:
    if emoji:
        message = Message(EMOJIS.get(emoji), original_msg)
    elif original_msg:
        message = transform(original_msg)
    else:
        message = Message()
    with contextlib.suppress(Exception):
        if not message.emoji:
            message.emoji = (
                ListPrompt(
                    "Choose a gitmoji:",
                    [
                        Choice(
                            emoji.to_string(),
                            emoji,
                        )
                        for emoji in EMOJIS.values()
                    ],
                    allow_filter=False,
                )
                .prompt()
                .data
            )
        message.content = InputPrompt(
            "Enter the commit title:",
            default_text=message.content,
            validator=lambda x: bool(x.strip()),
        ).prompt()
    return message.to_string()
