@echo off
title Gramma - Installing dependencies and creating shortcuts, please wait...

cd /d %~dp0

echo Verifying poetry...
pip install poetry

echo Installing gramma...
python -m poetry install
if %ERRORLEVEL% neq 0 (
    echo Installation failed. Please ensure Poetry is installed and try again.
    exit /b %ERRORLEVEL%
)

echo Creating shortcut...
powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%USERPROFILE%\Desktop\Gramma.lnk'); $Shortcut.TargetPath = '%CD%\gramma_starter.bat'; $Shortcut.WorkingDirectory = '%CD%'; $Shortcut.IconLocation = '%CD%\src\images\app_icon.ico'; $Shortcut.Description = 'Transform your clipboard into a smart text assistant.'; $Shortcut.Save()"

echo gramma has been installed successfully.
pause
