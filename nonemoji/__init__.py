from .cli import main as main
from .feature import Message as Message
from .feature import transform as transform

# def main(argv: Optional[List[str]]):
#     default_style = Style.from_dict(
#         {
#             "questionmark": "fg:#673AB7 bold",
#             "question": "",
#             "sign": "",
#             "unsign": "",
#             "selected": "",
#             "pointer": "bold",
#             "annotation": "",
#             "answer": "bold",
#         }
#     )

#     src_choices: List[Choice[str]] = [
#         Choice(
#             f"{emoji.emoji}{' '*(4-wcswidth(emoji.emoji))}- {emoji.description}",
#             emoji.name,
#         )
#         for emoji in emojis
#     ]
#     result = ListPrompt("Where to store the plugin?", src_choices).prompt(
#         style=default_style
#     )
