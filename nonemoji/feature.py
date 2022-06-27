import re
from dataclasses import dataclass
from typing import Optional, cast

from noneprompt import Choice, ListPrompt, InputPrompt

from .emoji import EMOJIS, Emoji

MESSAGE_REGEX = re.compile(r"^:(?P<emoji>\w+):(?P<message>[\s\S]+)$")


@dataclass
class Message:
    emoji: Optional[Emoji] = None
    message: Optional[str] = None

    @property
    def valid(self) -> bool:
        return bool(self.emoji and self.message)

    def to_string(self) -> str:
        if not self.valid:
            raise ValueError("Message is not valid")
        emoji = cast(Emoji, self.emoji)
        message = cast(str, self.message)
        return f"{emoji.code} {message.strip()}"


def transform(message: str) -> Message:
    match = MESSAGE_REGEX.match(message)
    if match:
        return Message(EMOJIS.get(match.group("emoji")), match.group("message"))
    return Message()


def prompt(original_msg: Optional[str] = None) -> str:
    message = transform(original_msg) if original_msg else Message()
    if not message.valid:
        message.message = InputPrompt("Message").prompt()
    return message.to_string()
