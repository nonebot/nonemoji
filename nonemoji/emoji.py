from dataclasses import dataclass

from wcwidth import wcswidth


@dataclass(frozen=True)
class Emoji:
    name: str
    emoji: str
    description: str

    @property
    def code(self) -> str:
        return f":{self.name}:"

    def to_string(self) -> str:
        return f"{self.emoji}{' ' * (4 - wcswidth(self.emoji))}- {self.description}"


EMOJIS = {
    emoji["name"]: Emoji(**emoji)
    for emoji in [
        {
            "emoji": "✨",
            "description": "Introduce new features.",
            "name": "sparkles",
        },
        {
            "emoji": "🐛",
            "description": "Fix a bug.",
            "name": "bug",
        },
        {
            "emoji": "📝",
            "description": "Add or update documentation.",
            "name": "memo",
        },
        {
            "emoji": "📄",
            "description": "Add or update license.",
            "name": "page_facing_up",
        },
        {
            "emoji": "🎨",
            "description": "Improve structure / format of the code.",
            "name": "art",
        },
        {
            "emoji": "♻️",
            "description": "Refactor code.",
            "name": "recycle",
        },
        {
            "emoji": "✅",
            "description": "Add, update, or pass tests.",
            "name": "white_check_mark",
        },
        {
            "emoji": "🚀",
            "description": "Deploy stuff.",
            "name": "rocket",
        },
        {
            "emoji": "💄",
            "description": "Add or update the UI and style files.",
            "name": "lipstick",
        },
        {
            "emoji": "🔖",
            "description": "Release / Version tags.",
            "name": "bookmark",
        },
        {
            "emoji": "🏷️",
            "description": "Add or update types.",
            "name": "label",
        },
        {
            "emoji": "🚨",
            "description": "Fix compiler / linter warnings.",
            "name": "rotating_light",
        },
        {
            "emoji": "➕",
            "description": "Add a dependency.",
            "name": "heavy_plus_sign",
        },
        {
            "emoji": "➖",
            "description": "Remove a dependency.",
            "name": "heavy_minus_sign",
        },
        {
            "emoji": "⬇️",
            "description": "Downgrade dependencies.",
            "name": "arrow_down",
        },
        {
            "emoji": "⬆️",
            "description": "Upgrade dependencies.",
            "name": "arrow_up",
        },
        {
            "emoji": "📌",
            "description": "Pin dependencies to specific versions.",
            "name": "pushpin",
        },
        {
            "emoji": "💚",
            "description": "Fix CI Build.",
            "name": "green_heart",
        },
        {
            "emoji": "👷",
            "description": "Add or update CI build system.",
            "name": "construction_worker",
        },
        {
            "emoji": "📈",
            "description": "Add or update analytics or track code.",
            "name": "chart_with_upwards_trend",
        },
        {
            "emoji": "🔧",
            "description": "Add or update configuration files.",
            "name": "wrench",
        },
        {
            "emoji": "🔨",
            "description": "Add or update development scripts.",
            "name": "hammer",
        },
        {
            "emoji": "🌐",
            "description": "Internationalization and localization.",
            "name": "globe_with_meridians",
        },
        {
            "emoji": "✏️",
            "description": "Fix typos.",
            "name": "pencil2",
        },
        {
            "emoji": "🎉",
            "description": "Begin a project.",
            "name": "tada",
        },
        {
            "emoji": "🚧",
            "description": "Work in progress.",
            "name": "construction",
        },
        {
            "emoji": "⏪️",
            "description": "Revert changes.",
            "name": "rewind",
        },
        {
            "emoji": "🔀",
            "description": "Merge branches.",
            "name": "twisted_rightwards_arrows",
        },
        {
            "emoji": "📦️",
            "description": "Add or update compiled files or packages.",
            "name": "package",
        },
        {
            "emoji": "👽️",
            "description": "Update code due to external API changes.",
            "name": "alien",
        },
        {
            "emoji": "🚚",
            "description": "Move or rename resources (e.g.: files, paths, routes).",
            "name": "truck",
        },
        {
            "emoji": "💥",
            "description": "Introduce breaking changes.",
            "name": "boom",
        },
        {
            "emoji": "♿️",
            "description": "Improve accessibility.",
            "name": "wheelchair",
        },
        {
            "emoji": "💡",
            "description": "Add or update comments in source code.",
            "name": "bulb",
        },
        {
            "emoji": "🍻",
            "description": "Write code drunkenly.",
            "name": "beers",
        },
        {
            "emoji": "🔊",
            "description": "Add or update logs.",
            "name": "loud_sound",
        },
        {
            "emoji": "🔇",
            "description": "Remove logs.",
            "name": "mute",
        },
        {
            "emoji": "🚸",
            "description": "Improve user experience / usability.",
            "name": "children_crossing",
        },
        {
            "emoji": "🏗️",
            "description": "Make architectural changes.",
            "name": "building_construction",
        },
        {
            "emoji": "🙈",
            "description": "Add or update a .gitignore file.",
            "name": "see_no_evil",
        },
        {
            "emoji": "🚩",
            "description": "Add, update, or remove feature flags.",
            "name": "triangular_flag_on_post",
        },
        {
            "emoji": "🥅",
            "description": "Catch errors.",
            "name": "goal_net",
        },
        {
            "emoji": "🗑️",
            "description": "Deprecate code that needs to be cleaned up.",
            "name": "wastebasket",
        },
        {
            "emoji": "⚰️",
            "description": "Remove dead code.",
            "name": "coffin",
        },
        {
            "emoji": "🧑‍💻",
            "description": "Improve developer experience",
            "name": "technologist",
        },
        {
            "emoji": "⚡️",
            "description": "Improve performance.",
            "name": "zap",
        },
        {
            "emoji": "🔥",
            "description": "Remove code or files.",
            "name": "fire",
        },
        {
            "emoji": "🍱",
            "description": "Add or update assets.",
            "name": "bento",
        },
    ]
}
