@echo off
pushd %~dp0
powershell -Command Set-ExecutionPolicy Bypass -scope CurrentUser -force || exit /b 1
powershell -File build.ps1 %* || exit /b 1
popd
