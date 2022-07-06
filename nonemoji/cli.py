from argparse import REMAINDER, ArgumentParser
from typing import Any, List, Callable, Optional

from .command import handle_hook, handle_list, handle_commit

parser = ArgumentParser("nonemoji", description="Simple gitmoji cli written in python")
_subparsers = parser.add_subparsers(title="subcommands")

# hook
hook_parser = _subparsers.add_parser("hook", help="Run as a git hook.")
hook_parser.add_argument("commit_msg_file", help="Path to the commit message file")
hook_parser.set_defaults(func=handle_hook)

# commit
commit_parser = _subparsers.add_parser("commit", help="Run as an independent tool.")
commit_parser.add_argument("-e", "--emoji", help="Emoji to use")
commit_parser.add_argument("-m", "--message", help="Commit message")
commit_parser.add_argument(
    "--", nargs=REMAINDER, help="Argument to pass to the git", dest="args"
)
commit_parser.set_defaults(func=handle_commit)

# list
list_parser = _subparsers.add_parser("list", help="List all available emoji.")
list_parser.set_defaults(func=handle_list)


def main(argv: Optional[List[str]] = None):
    result = parser.parse_args(argv)
    result = vars(result)
    func: Callable[..., Any] = result.pop("func")
    func(**result)
