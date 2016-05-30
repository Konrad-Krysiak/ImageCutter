@echo off
cd /d %~dp0\resources
.\python-2.7.11.msi
echo -installing python

set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib
echo -adding PYTHON environment variable to PYTHONPATH
setx path "%path%;C:\Python27;"
echo -adding PYTHON environment variable to PATH

python get-pip.py 
echo -installing pip
setx path "%path%;C:\Python\Scripts;"
echo -adding PIP environment variable to PATH

pip install Pillow
echo -installing pillow

pause