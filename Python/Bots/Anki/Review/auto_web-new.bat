@echo off
:: If the script was already relaunched minimized, go to the main logic
if "%~1"=="/minimized" goto start

:: Relaunch this batch file in a new CMD window minimized
powershell -Command "Start-Process 'cmd.exe' -ArgumentList '/c \"%~f0\" /minimized' -WindowStyle Minimized"
exit

:start
:: Your actual commands start here
powershell.exe pyenv shell 3.10.11
powershell.exe python "C:\_Backup\Github\VisualStudioCode\Python\Bots\Anki\Review\auto_web.py"
