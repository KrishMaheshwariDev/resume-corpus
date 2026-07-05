@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-resume.ps1" %*
