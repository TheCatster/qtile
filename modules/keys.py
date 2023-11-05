import os

from libqtile.config import Key
from libqtile.lazy import lazy

from modules.common import mod, terminal
from modules.lazy_functions import (
    move_focus_to_next_screen,
    move_focus_to_prev_screen,
    move_window_to_next_screen,
    move_window_to_prev_screen,
)

# Preferred
HOME = os.path.expanduser("~")
BROWSER = "google-chrome-stable"

keys = [
    # Switch focus between windows/screens
    # Key([mod], "h", move_focus_to_prev_screen, desc="Move focus to left"),
    # Key([mod], "l", move_focus_to_next_screen, desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod],
        "space",
        lazy.layout.swap_main(),
        desc="Swap current window to main pane",
    ),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # # Grow windows. If current window is on the edge of screen and direction
    # # will be to screen edge - window would shrink.
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    # Qtile
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
]

spawn_apps = [
    # ===== Core =====
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod],
        "d",
        lazy.spawn('rofi -show-icons -show drun'),
        desc="Spawn rofi",
    ),
    # ===== Browser =====
    Key([mod], "w", lazy.spawn(f"{BROWSER}"), desc="Launch browser"),
    # ===== Misc Apps =====
    Key([mod], "c", lazy.spawn("discord-canary"), desc="Launch Discord"),
    Key([mod], "s", lazy.spawn("signal-desktop"), desc="Launch Signal"),
    Key([mod], "m", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Launch Pavucontrol"),
    # ===== Media Control =====
    # Volume
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+"),
        desc="Raise volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
        desc="Lower volume",
    ),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), desc="Toggle mute"),
    # ===== Screenshot =====
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Print-screen area"),
    Key(
        ["control"],
        "Print",
        lazy.spawn(f"flameshot full -c -p {HOME}/Screenshots"),
        desc="Print-screen full-screen",
    ),
]

keys.extend(spawn_apps)
