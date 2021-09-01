@echo off
set local

set PYTHONPATH=%systemdrive%/GRL/Thread1.2/Thread_Harness;

set file=%1
for /f "tokens=1* delims==" %%I in ('wmic path win32_pnpentity get HardwareID /format:list ^| find "PID_521"') do (
	echo "%%~J"
	for %%f  in ("%%~J" get caption /format:list ^| find "USB Serial Device"') do (
	
		echo "%%~B"
		call :setCOM "%%~B"
	)
)




:: display all COM* varibles
echo:
echo:
echo "Found Devices"
set _COM
:: end main batch
goto :EOF

:setCOM <WMIC_output_line>
:: sets _COM#=line
setlocal
set "str=%~1"
set "num=%str:*(COM=%"
set "num=%num:)=%"
echo:
echo:
echo  "#######################Flashing Device COM:"%num:)=%"##########################
"%systemdrive%\GRL\Thread1.2\Python27\python.exe" nrf_burn.py -d com"%num:)=%" -i %file%
set str=%str:(COM=&rem.%
endlocal & set "_COM%num%=%str%"
goto :EOF