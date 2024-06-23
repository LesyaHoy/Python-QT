************************************** Creating virtual enviroment in the current directory **************************************
@echo off
echo *** Remove old virtual environment
rd /s /q .\venv\
echo *** Create new virtual environment
PYTHON_PATH -m venv .\venv
echo *** Install required packages
.\venv\Scripts\pip install -r requirements.txt
echo *** list all modules
.\venv\Scripts\pip list

************************************** requirements.txt *********************************************************************
PySide6==6.5.1.1
PySide6-Addons==6.5.1.1
PySide6-Essentials==6.5.1.1

************************************* createing py files from resources ******************************************************
@echo off
echo Create resources files
FOR /R %%I IN (*.ui) DO  .\venv\Scripts\pyside6-uic "%%I" -o "%%~pI\Ui_%%~nI.py"
FOR /R %%I IN (*.qrc) DO  .\venv\Scripts\pyside6-rcc -g python -o "%%~pI\%%~nI_rc.py" "%%I"
rem FOR /R %%I IN (*_rc.py) DO powershell -Command "(gc "%%I") -replace 'PySide6', 'PyQt6' | Out-File -encoding ASCII "%%I"

******************************************************************************************************************************

