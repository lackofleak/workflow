
from libqtile import bar, layout, widget , hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os , time
from notifypy import Notify


# My fnc 

@lazy.function
def vol_in(qtile):
    notification = Notify()
    notification.title = "Volume"
    notification.message = "Increas +5"
    notification.icon = "/home/amir/.config/qtile/audio-volume/audio-volume-high.svg"
    notification.send()
    os.system("pactl -- set-sink-volume 0 +5%")

@lazy.function
def vol_de(qtile):
    notification = Notify()
    notification.title = "Volume"
    notification.message = "Decrease -5"
    notification.icon = "/home/amir/.config/qtile/audio-volume/audio-volume-low.svg"
    notification.send()
    os.system("pactl -- set-sink-volume 0 -5%")

@lazy.function
def vol_m(qtile):
    notification = Notify()
    notification.title = "Volume"
    notification.message = "Muted / unMuted"
    notification.icon = "/home/amir/.config/qtile/audio-volume/audio-volume-muted.svg"
    notification.send()
    os.system("pactl set-sink-mute @DEFAULT_SINK@ toggle")

@lazy.function
def sc_shot(qtile):
    notification = Notify()
    notification.title = "Screen shot"
    notification.message = "take in 5 sec"
    notification.icon = "/home/amir/.config/qtile/scshot1.svg"
    notification.send()
    os.system("scrot -d 5")


# @lazy.function
# def br_in(qtile):
#     notification = Notify()
#     notification.title = "Brightness"
#     notification.message = "Increas 10%"
#     #notification.audio = "/home/amir/.config/qtile/notif.wav"
#     notification.icon = "/home/amir/.config/qtile/brightness.png"
#     notification.send()
#     os.system("sudo light -A 10")

# @lazy.function
# def br_de(qtile):
#     notification = Notify()
#     notification.title = "Brightness"
#     notification.message = "Decrease 10%"
#     # notification.audio = "/home/amir/.config/qtile/notif.wav"
#     notification.icon = "/home/amir/.config/qtile/brightness.png"
#     notification.send()
#     os.system("sudo light -U 10")



mod = "mod4"

keys = [
    # Move WM to WorkSpace :
    Key([mod, "shift"], "1", lazy.window.togroup("")),
    Key([mod, "shift"], "2", lazy.window.togroup(" ")),
    Key([mod, "shift"], "3", lazy.window.togroup("  ")),
    Key([mod, "shift"], "4", lazy.window.togroup("  ")),
    # Switch to WorkSpace :
    Key([mod],"1",lazy.group[""].toscreen(),),
    Key([mod],"2",lazy.group[" "].toscreen(),),
    Key([mod],"3",lazy.group["  "].toscreen(),),
    Key([mod],"4",lazy.group["  "].toscreen(),),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Moving Windows to L/R/U/D
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. 
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # Toggle between split and unsplit sides of stack.
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Term :
    Key([mod], "Return", lazy.spawn("alacritty -e fish"), desc="Launch terminal"),
    # QtilE
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([mod], "f" , lazy.window.toggle_fullscreen() , desc="Full screen"),
    Key([mod], "s" , sc_shot() , desc="take screen shot"),
    #XF86 ?
    Key([], "XF86AudioLowerVolume", vol_de()),
    Key([], "XF86AudioRaiseVolume", vol_in()),
    Key([], "XF86AudioMute", vol_m()),
]


groups = [
    Group(""),
    Group(" "),
    Group("  "),
    Group("  ")
]




#Let's Tile !
layouts = [
    layout.Columns(
        border_focus="#81c8be",
        border_focus_stack="#85c1dc",
        border_normal="#cdd6f4",
        border_on_single=True,
        border_width=3,
        margin=[2,8,7,8],
        margin_on_single=[20,30,30,30]
    ),
]



widget_defaults = dict(
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   #simple power Menue: +> commands mybe diiferent with your DT !

                widget.WidgetBox(widgets=[
                     widget.TextBox( #power
                        "  " ,
                        fontsize=16 ,
                        foreground = "#BF616A",
                        mouse_callbacks={'Button1': lazy.spawn("doas shutdown -h now")}
                        ),
                     widget.TextBox( #restart
                        "",
                        fontsize=16,
                        foreground = "#A3BE8C",
                        mouse_callbacks={'Button1': lazy.spawn("doas reboot")}
                        ),
                     widget.TextBox( #L0gout -> Kill Qtile !
                        "   ",
                        fontsize=16,
                        foreground = "#B48EAD",
                        mouse_callbacks={'Button1': lazy.shutdown()}
                        ),
                     ],
                    fontsize=16,
                    foreground="#a6e3a1",
                    text_closed="   amir ",
                    text_open="  "
                ),

                widget.GroupBox(
                    active="#5E81AC",
                    block_highlight_text_color="#88C0D0",
                    fontsize=16,
                    padding=1,
                    borderwidth=0,
                ),

                widget.Prompt(
                    foreground="#5E81AC",
                    fontsize=18,
                    prompt=' ',
                    bell_style='audible',
                    cursor_color="#4C566A"
                ),

                widget.Spacer(),

                #Key = mod4 + Space
                widget.KeyboardLayout(
                    configured_keyboards=["us","ir"],
                    fmt=' {}',
                    foreground="#cdd6f4",
                    fontsize=16
                ),

                #don't forget to install Pavucontrol 
                widget.PulseVolume(
                    fmt=' 󰕾 {} ',
                    fontsize=16,
                    foreground="#88C0D0",
                    volume_app="pavucontrol"
                ),



                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    brightness_file="brightness",
                    fmt="󰃟  {} ",
                    fontsize=16,
                    foreground="#BF616A"
                ),


                widget.Wlan(
                    interface="wlo1",
                    disconnected_message=" 󰤭 ",
                    format='{essid} {percent:2.0%}',
                    fontsize=16,
                    foreground="#b4befe",
                    fmt="󱚻  {} "
                    
                ),

                widget.Battery(
                    fontsize=16,
                    charge_char="  ",
                    discharge_char="󰠠 ",
                    empty_char=" 󱃍 ",
                    full_char=" 󱟢 ",
                    low_foreground="#BF616A",
                    low_percentage=0.3,
                    notify_below=0.3,
                    format="{char} {percent:2.0%}",
                    foreground="#8FBCBB"
                ),


                widget.Clock(
                    fontsize=15,
                    foreground="#c6a0f6",
                    format="%a, %H:%M %p ",
                    fmt=" 󱑆  {}"
                ),
                widget.Systray(icon_size=18),
                widget.Spacer(length=8)
            ],
            37,
            margin=[8,8,5,8],
            background="#1e2030"
           
        ),
        wallpaper_mode="fill",
        wallpaper="/home/amir/Pictures/04.jpg",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"

#startup
@hook.subscribe.startup_once
def autostart():
    os.system("bash /home/amir/.config/start.sh")
