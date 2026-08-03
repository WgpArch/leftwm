# Look & Feel (Theming)

The entire setup revolves around a "Cyberpunk Taxi" aesthetic, utilizing a warm amber and coral color palette against a deep black background.

## 🎨 Color Palette

| Role | Hex Code | Description |
| :--- | :--- | :--- |
| **Border** | `#C36C0F` | Rich Amber (Used for Polybar borders, Rofi borders, and selected items) |
| **Text** | `#ED9381` | Soft Coral (Primary text color for high readability) |
| **Background** | `#0a0a0a` | Deep Black (Base background) |
| **Highlight** | `#FFB86C` | Light Amber (Used for active workspaces and secondary text) |

## 🪟 Rofi Theme

The Rofi menus use a heavily customized version of the `fancy2` theme (`~/.config/leftwm/rofi/fancy2.rasi`). 

**Key Features:**
*   **Background Image:** The `Taxigirl_resized.jpg` image is applied directly to the Rofi window background.
*   **Transparency:** The `mainbox` is set to transparent so the wallpaper bleeds through the menu items.
*   **Rounded Corners:** Both the main window and the selected elements feature rounded corners (`border-radius: 12px` and `6px` respectively).

## 🖼️ Wallpaper

The desktop wallpaper is set using `feh` via the LeftWM `up` script. 
*   **Original Image:** `~/Pictures/ALNW/Taxigirl.jpg` (Used for the desktop background).
*   **Resized Image:** `~/Pictures/ALNW/Taxigirl_resized.jpg` (Cropped and scaled specifically to fit the Rofi window dimensions without tiling).
