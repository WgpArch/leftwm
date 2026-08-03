# Polybar Configuration

The status bar is handled by **Polybar**, configured to float at the top of the screen with rounded corners. The configuration files are located in `~/.config/polybar1/`.

## 📐 Layout

The bar is divided into three distinct sections:

*   **Left:** Arch Linux launcher icon (triggers Rofi) and the system tray (`nm-applet`).
*   **Center:** 15 Workspaces (Tags), Date/Time, and a live Weather module.
*   **Right:** System statistics (Memory, CPU, Temperature, Filesystem) and a Power menu icon.

## 🖱️ Click Handlers & Rofi Menus

Several modules are interactive and launch custom Rofi menus styled with the cyberpunk theme:

*   **Launcher (`Mod4 + p` or click the Arch icon):** Opens the application launcher.
*   **Weather:** Clicking the weather module opens a detailed forecast window.
*   **Calendar:** Clicking the clock opens a monthly calendar view.
*   **Power Menu:** Clicking the power icon opens a menu to Lock, Logout, Reboot, Shutdown, or Suspend.

## ⚙️ Scripts

All custom scripts are located in `~/.config/polybar1/`:
*   `launch.sh`: Safely kills existing instances and launches the bar.
*   `weather.py`: Fetches weather data from `wttr.in`.
*   `polybar_calendar.py`: Generates the calendar text.
*   `click_*.sh`: Shell scripts that pipe the Python script outputs into Rofi.
