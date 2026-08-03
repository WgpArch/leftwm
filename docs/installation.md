# Installation Guide

This guide will help you set up my LeftWM configuration on your Arch Linux system.

## 1. Prerequisites

Ensure you have the following packages installed. You can install them via `pacman` or your preferred AUR helper (like `paru` or `yay`):

```bash
# Window Manager & Bar
sudo pacman -S polybar
trizen -S leftwm

# Utilities & Menu
sudo pacman -S rofi feh slock network-manager-applet

# Fonts (Required for icons and text)
sudo pacman -S ttf-font-awesome noto-fonts
# Note: Ensure you have 'Z003 Bold Italic' installed (often available via AUR or manual install)

git clone https://github.com/WgpArch/leftwm.git ~/.dotfiles/leftwm
cd ~/.dotfiles/leftwm
# Link LeftWM configs
ln -sf ~/.dotfiles/leftwm/configs/leftwm/config.ron ~/.config/leftwm/config.ron
ln -sf ~/.dotfiles/leftwm/configs/leftwm/rofi ~/.config/leftwm/rofi

# Link Polybar configs
ln -sf ~/.dotfiles/leftwm/configs/polybar/leftwm ~/.config/polybar1

# Create the theme symlink (Crucial for LeftWM to find the up script and theme.toml)
mkdir -p ~/.config/leftwm/themes
ln -sf ~/.dotfiles/leftwm/configs/leftwm ~/.config/leftwm/themes/cyberpunk
ln -sf ~/.config/leftwm/themes/cyberpunk ~/.config/leftwm/themes/current

Set permissions
chmod +x ~/.config/leftwm/themes/current/up
chmod +x ~/.config/leftwm/rofi/powermenu.sh
chmod +x ~/.config/polybar1/launch.sh
chmod +x ~/.config/polybar1/click_weather.sh
chmod +x ~/.config/polybar1/click_calendar.sh
chmod +x ~/.config/polybar1/weather.py
chmod +x ~/.config/polybar1/polybar_calendar.py

