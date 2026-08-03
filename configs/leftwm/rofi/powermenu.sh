#!/bin/bash

# Get the selected option
selected=$(cat ~/.config/leftwm/rofi/powermenu_options | rofi -dmenu -i -theme ~/.config/leftwm/rofi/fancy2.rasi -p "Power")

case "$selected" in
    *"Lock"*)
        slock
        ;;
    *"Logout"*)
        loginctl kill-session $XDG_SESSION_ID
        ;;
    *"Reboot"*)
        systemctl reboot
        ;;
    *"Shutdown"*)
        systemctl poweroff
        ;;
    *"Suspend"*)
        systemctl suspend
        ;;
esac
