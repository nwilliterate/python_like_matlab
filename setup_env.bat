@echo off
REM Automated virtual environment setup script for Windows

echo ====================================
echo Python Like MATLAB - Environment Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed.
    echo Please install Python 3.7 or higher: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Python version check completed
python --version
echo.

REM Create virtual environment
if exist venv (
    echo [INFO] Virtual environment already exists.
    choice /C YN /M "Do you want to delete the existing environment and recreate it?"
    if errorlevel 2 goto activate_env
    if errorlevel 1 (
        echo [INFO] Removing existing virtual environment...
        rmdir /s /q venv
    )
)

echo [2/3] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment.
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment created successfully.
echo.

:activate_env
REM Activate virtual environment and install packages
echo [3/3] Installing packages...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install packages.
    pause
    exit /b 1
)

echo.
echo ====================================
echo Installation completed successfully!
echo ====================================
echo.
echo To activate the virtual environment:
echo     venv\Scripts\activate
echo.
echo Run MATLAB-style interpreter:
echo     python matlab_interpreter.py
echo.
echo Run simple MATLAB REPL:
echo     python matlab_repl.py
echo.
echo Run Jupyter Notebook:
echo     jupyter notebook examples/
echo.
pause
