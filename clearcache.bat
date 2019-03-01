@echo off

cd src && rmdir /s /q __pycache__
cd .. && rmdir /s /q -R tmp

exit
