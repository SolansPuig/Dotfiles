# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

from settings import COLS, FONT_PARAMS, WITH_SYS_TRAY

from typing import List  # noqa: F401
from widgets import ShellScript

import json
import os
pycolors = os.path.expanduser('~/.cache/wal/colors.json')
colors = json.loads(open(pycolors).read())

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("amixer -c 0 sset Master 2- unmute")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 sset Master 2+ unmute")),
    Key([], "Print",
        lazy.spawn("scrot /home/roger/Images/Screenshots/%Y-%m-%d-%T-screenshot.png")),
    Key(["shift"], "Print",
        lazy.spawn("scrot -u /home/roger/Images/Screenshots/%Y-%m-%d-%T-screenshot.png")),

]

group_names = [
        (u" \uFCB5 ", {"layout": "monadtall", "spawn": "urxvt"}),
        (u" \uF738 ", {"layout": "monadtall"}),
        (u" \uFB71 ", {"layout": "monadtall"}),
        (u" \uF718 ", {"layout": "monadtall"}),
        (u" \uF7E8 ", {"layout": "monadtall"}),
        (u" \uF1B6 ", {"layout": "monadtall"}),
        #(u'7 \uF1B6 ', {"layout": "monadtall"}),
        #(u'8 \uF1B6 ', {"layout": "monadtall"}),
        #(u'9 \uF1B6 ', {"layout": "monadtall"})
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {
        "border_width": 2,
        "margin": 4,
        "border_focus": colors["colors"]["color14"],
        "border_normal": colors["special"]["background"],
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font='RobotoMono Nerd Font Medium',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text = ' ◢',
                    foreground = colors["colors"]["color6"],
                    fontsize = 50,
                    padding = -8
                ),
                widget.GroupBox(
                    this_current_screen_border = colors["colors"]["color5"], 
                    background = colors["colors"]["color6"],
                    rounded = False,
                    highlight_method = "block",
                    inactive = colors["special"]["background"],
                    active = colors["special"]["background"],
                    margin = 0,
                    padding_x = 5,
                    padding_y = 3,
                    borderwidth = 1,
                    font = 'Roboto Mono Nerd Font',
                    fontsize = 18
                ),
                widget.TextBox(
                    text = '◤ ', 
                    foreground = colors["colors"]["color6"],
                    fontsize = 50, 
                    padding = -8
                ),
                widget.Prompt(
                    prompt = "$ : ",
                    cursor_color = colors["special"]["foreground"],
                    foreground = colors["special"]["foreground"],
                    bell_style = "visual",
                ),
                widget.Spacer(),
                widget.TextBox(
                    text = u'◢',
                    foreground = colors["colors"]["color3"],
                    fontsize = 50,
                    padding = -8
                ),
                widget.CurrentLayout(
                    background = colors["colors"]["color3"],
                    foreground = colors["special"]["background"],
                ),
                widget.TextBox(
                    text = '◤',
                    foreground = colors["colors"]["color3"],
                    background = colors["colors"]["color4"],
                    fontsize = 50,
                    padding = -8

                ),
                widget.TextBox(
                    foreground = colors["special"]["background"],
                    background = colors["colors"]["color4"],
                    text = u'\ufaa8',
                ),
                widget.Wlan(
                    foreground = colors["special"]["background"],
                    background = colors["colors"]["color4"],
                    disconnected_message = "Desconnectat",
                    format = "{essid}",
                    interface = "wlp2s0"
                ),
                widget.TextBox(
                    text = '◤',
                    foreground = colors["colors"]["color4"],
                    background = colors["colors"]["color5"],
                    fontsize = 50,
                    padding = -8

                ),
                widget.TextBox(
                    foreground = colors["special"]["background"],
                    background = colors["colors"]["color5"],
                    text = u'\ufa7d',
                ),
                widget.Volume(
                    foreground = colors["special"]["background"],
                    background = colors["colors"]["color5"],
                ),
                widget.TextBox(
                    text = '◤',
                    foreground = colors["colors"]["color5"],
                    fontsize = 50,
                    padding = -8

                ),
                widget.Clock(
                    foreground = colors["special"]["foreground"],
                    format = '%A, %d %B - %H:%M '
                ),
            ],
            25,
            background =colors["special"]["background"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
