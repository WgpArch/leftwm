#!/bin/bash
python ~/.config/polybar1/weather.py --details | rofi -dmenu -p "Weather" -theme ~/.config/leftwm/rofi/fancy2.rasi

