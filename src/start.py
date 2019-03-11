#MIT License
#
#Copyright (c) 2019 thatswhereurwrongkiddo
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#start.py
#the initial program the user encounters when running otpy for
#the first time

#import version variable from __init__ file and os module
from __init__ import ver, title
import os
from otpy_func_premain import checksys

os.system("cd .. && start clearcache.bat")

checksys()
#define functions
def pause():
    input("Press ENTER to continue...")

#greet user
print("Welcome to otpy v{0}: The (Python) Oregon Trail!".format(ver))
print()
pause()

#open menu
os.system("python -B init_menu.py")
