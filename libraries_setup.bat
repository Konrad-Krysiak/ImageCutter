@echo off
cd /d %~dp0\resources

echo - installing pip
python get-pip.py 
echo - done

timeout 5

echo - installing pillow
pip install Pillow
echo - done


timeout 2