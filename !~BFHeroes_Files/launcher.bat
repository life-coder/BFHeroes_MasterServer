@echo off
title Battlefield Heroes Launcher

del /q /f "%temp%\base64"  >nul 2>nul
del /q /f "%temp%\decoded"  >nul 2>nul
del /q /f "%temp%\error_message.vbs"  >nul 2>nul

REG QUERY "HKEY_CLASSES_ROOT\bfheroes\shell\open\command" >nul 2>nul
if %ERRORLEVEL%==1 goto LAUNCHER_INSTALLER

if "%*"=="" goto NO_LAUNCH_COMMAND

setlocal ENABLEEXTENSIONS
set KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\EA Games\Battlefield Heroes"
set VALUE_NAME="Install Dir"

REG QUERY %KEY_NAME% /v %VALUE_NAME% >nul 2>nul
if %ERRORLEVEL%==1 goto NO_REQUIRED_REG

FOR /F "usebackq tokens=3*" %%A IN (`REG QUERY %KEY_NAME% /v %VALUE_NAME%`) DO (
    set InstallDir=%%B
    )

set base64=%*
set base64=%base64:bfheroes://=%
set base64=%base64:/=%

@echo %base64% > "%temp%\base64"

certutil /decode "%temp%\base64" "%temp%\decoded" >nul 2>nul

for /f "useback tokens=* delims=" %%# in ("%temp%\decoded")  do set "decoded=%%#"
cd /D %InstallDir%

set decoded=%decoded:/=\%
set decoded=%decoded:\data=/data%

start bfheroes.exe %decoded%

del /q /f "%temp%\base64"  >nul 2>nul
del /q /f "%temp%\decoded"  >nul 2>nul

exit

:LAUNCHER_INSTALLER
@echo X=MsgBox("Do you want to install Battlefield Heroes Launcher registry to your computer?" + vbNewLine + "This will allow to run Battlefield Heroes from Master Server Emulator website!",vbYesNo + vbQuestion,"Battlefield Heroes Launcher") > "%temp%\error_message.vbs"
@echo If X = VbYes Then >> "%temp%\error_message.vbs"
@echo    WScript.Quit(0) >> "%temp%\error_message.vbs"
@echo Else >> "%temp%\error_message.vbs"
@echo    WScript.Quit(1) >> "%temp%\error_message.vbs"
@echo End If >> "%temp%\error_message.vbs"
wscript "%temp%\error_message.vbs"
if %ERRORLEVEL%==0 goto INSTALL

del /q /f "%temp%\error_message.vbs"  >nul 2>nul
exit

:INSTALL
echo Installing... Please wait...
del /q /f "%temp%\error_message.vbs"  >nul 2>nul
set base64=V2luZG93cyBSZWdpc3RyeSBFZGl0b3IgVmVyc2lvbiA1LjAwDQoNCltIS0VZX0NMQVNTRVNfUk9PVFxiZmhlcm9lc10NCkA9IlVSTDpiZmhlcm9lcyBQcm90b2NvbCINCiJVUkwgUHJvdG9jb2wiPSIiDQoNCltIS0VZX0NMQVNTRVNfUk9PVFxiZmhlcm9lc1xzaGVsbF0NCg0KW0hLRVlfQ0xBU1NFU19ST09UXGJmaGVyb2VzXHNoZWxsXG9wZW5dDQoNCltIS0VZX0NMQVNTRVNfUk9PVFxiZmhlcm9lc1xzaGVsbFxvcGVuXGNvbW1hbmRdDQpAPSJMQVVOQ0hFUl9MT0NBVElPTiAlMSINCg0KW0hLRVlfTE9DQUxfTUFDSElORVxTT0ZUV0FSRVxXT1c2NDMyTm9kZVxFQSBHYW1lc1xCYXR0bGVmaWVsZCBIZXJvZXNdDQoiSW5zdGFsbCBEaXIiPSJJTlNUQUxMX0xPQ0FUSU9OIg0K
@echo %base64% > "%temp%\base64"
certutil /decode "%temp%\base64" "%temp%\decoded" >nul 2>nul
set curr_loc=%cd%\%~n0%~x0
set fixed_loc=%curr_loc:\=\\%
powershell -Command "(gc %temp%\decoded) -replace 'LAUNCHER_LOCATION', '%fixed_loc%' | Out-File %temp%\bfheroes_install.temp"
set curr_loc=%cd%
set fixed_loc=%curr_loc:\=\\%
powershell -Command "(gc %temp%\bfheroes_install.temp) -replace 'INSTALL_LOCATION', '%fixed_loc%' | Out-File %temp%\BFHeroes_install.reg"
regedit %temp%\BFHeroes_install.reg >nul 2>nul
if %ERRORLEVEL%==5 goto INSTALL_FAIL
cls
@echo X=MsgBox("Installed successfully!"  + vbNewLine + "You can now launch game!",0+64,"Battlefield Heroes Launcher") > "%temp%\error_message.vbs"
wscript "%temp%\error_message.vbs"
del /q /f "%temp%\error_message.vbs"  >nul 2>nul
del /q /f "%temp%\bfheroes_install.temp"  >nul 2>nul
del /q /f "%temp%\BFHeroes_install.reg"  >nul 2>nul
del /q /f "%temp%\base64"  >nul 2>nul
del /q /f "%temp%\decoded"  >nul 2>nul
exit

:INSTALL_FAIL
cls
@echo X=MsgBox("Can't write required registry keys because you don't have administrator rights!",0+16,"Battlefield Heroes Launcher") > "%temp%\error_message.vbs"
wscript "%temp%\error_message.vbs"
del /q /f "%temp%\error_message.vbs"  >nul 2>nul
del /q /f "%temp%\bfheroes_install.temp"  >nul 2>nul
del /q /f "%temp%\BFHeroes_install.reg"  >nul 2>nul
del /q /f "%temp%\base64"  >nul 2>nul
del /q /f "%temp%\decoded"  >nul 2>nul
exit

:NO_LAUNCH_COMMAND
@echo X=MsgBox("You should launch Battlefield Heroes from Master Server Emulator website!",0+48,"Battlefield Heroes") > "%temp%\error_message.vbs"
wscript "%temp%\error_message.vbs"
del /q /f "%temp%\error_message.vbs"  >nul 2>nul
exit

:NO_REQUIRED_REG
@echo X=MsgBox("Cannot find correct registry key for Battlefield Heroes!" + vbNewLine + "Please 'Repair Game' in Origin!",0+16,"Battlefield Heroes") > "%temp%\error_message.vbs"
wscript "%temp%\error_message.vbs"
del /q /f "%temp%\error_message.vbs"  >nul 2>nul
exit

