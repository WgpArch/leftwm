#!/bin/bash

# Run the calendar script and pipe to Rofi
python3 ~/.config/polybar1/polybar_calendar.py | rofi -dmenu -i -theme ~/.config/leftwm/rofi/fancy2.rasi -p "Calendar"
