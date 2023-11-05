from libqtile.config import Group, Key, KeyChord, Match
from libqtile.lazy import lazy

from modules.common import host, mod
from modules.state import toggling_state


group_keys = []
num_groups = [Group(i) for i in "123456789"]
other_groups = []

for group in num_groups:
    group_keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}",
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name),
                desc=f"move focused window to group {group.name}",
            ),
            # mod + ctrl + group = toggle pressed group
            Key(
                [mod, "control"],
                group.name,
                lazy.group[group.name].function(
                    lambda pressed_group: toggling_state.toggle_group(pressed_group)
                ),
                desc=f"Toggle group {group.name}",
            ),
        ]
    )


app_keychord = KeyChord([mod], "space", [])
other_groups.append(
    Group(
        name="Music",
        exclusive=False,
        spawn="spotify",
        matches=[Match(wm_class="Spotify", title="Spotify")],
        init=True,
    )
)
app_keychord.submappings.extend(
    [
        Key(
            [],
            "m",
            lazy.group["Music"].toscreen(),
            desc="Focus Music group",
        ),
    ]
)


if host == "generation":
    # I don't want Discord to be last so I user insert
    other_groups.insert(
        -1,
        Group(
            name="Discord",
            spawn="discord-canary",
            matches=[Match(wm_class="discord")],
            init=True,
        ),
    )
    other_groups.insert(
        -1,
        Group(
            name="Thunderbird",
            spawn="thunderbird",
            matches=[Match(wm_class="thunderbird")],
            init=True,
        ),
    )
    app_keychord.submappings.extend(
        [
            Key(
                [],
                "d",
                lazy.group["Discord"].toscreen(),
                desc="Focus Discord group",
            ),
            Key(
                [],
                "t",
                lazy.group["Thunderbird"].toscreen(),
                desc="Focus Thunderbird group",
            ),
        ]
    )

group_keys.append(app_keychord)

groups = []
groups.extend(num_groups)
groups.extend(other_groups)
