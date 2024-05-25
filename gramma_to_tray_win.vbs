Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "poetry run python gramma.py", 0
Set WshShell = Nothing
