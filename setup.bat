@echo off
cd /d %~dp0
echo - installing python
.\resources\python-2.7.11.msi
echo - done
echo - When python is already installed press any key to continue...


timeout 600

echo - adding PYTHON and PIP environment variable to PATH
setx PATH "%PATH%;C:\Python27;C:\Python27\Scripts;"
echo - done


timeout 2