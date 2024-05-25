#!/bin/bash
echo "Verifying poetry..."
pip install poetry
echo "Installing gramma..."
poetry install
if [ $? -ne 0 ]; then
    echo "Installation failed. Please ensure Poetry is installed and try again."
    exit 1
fi

echo "Creating shortcut..."
SHORTCUT_PATH="$HOME/Desktop/Gramma.desktop"
echo "[Desktop Entry]" > "$SHORTCUT_PATH"
echo "Version=1.0.0" >> "$SHORTCUT_PATH"
echo "Type=Application" >> "$SHORTCUT_PATH"
echo "Description=Transform your clipboard into a smart text assistant." >> "$SHORTCUT_PATH"
echo "Terminal=false" >> "$SHORTCUT_PATH"
echo "Exec=$PWD/gramma_starter.sh" >> "$SHORTCUT_PATH"
echo "Name=Gramma" >> "$SHORTCUT_PATH"
echo "Comment=Start Gramma" >> "$SHORTCUT_PATH"
echo "Icon=$PWD/src/images/app_icon.ico" >> "$SHORTCUT_PATH"
chmod +x "$SHORTCUT_PATH"

echo "gramma has been installed successfully."
