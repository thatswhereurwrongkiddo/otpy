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

#init_menu.py
#initial menu for otpy program

#import colorama module for menu
import colorama
from __init__ import ver, title
import os
from otpy_func_premain import clearscreen, checksys
from color_storage import txtc_wb, bgc_wb, resetc_wb

clearscreen()

#initialize colorama settings


#print main menu
print(txtc_wb + bgc_wb + "otpy Main Menu:")
print("               ")
print("Your options are as follows:")
print("                            ")
print("1. Travel The Trail         ")
print("2. End                      ")
print("                            ")
u_ch = input("And you choose?: ")
print(resetc_wb)

#if/else statement for player selection
import time
if u_ch == "1" or u_ch.lower() == "travel" or u_ch.lower() == "travel the trail":
    os.system("python -B main.py")
elif u_ch == "2" or u_ch.lower() == "end":
    pass
else:
    print("Unrecognized input, try again")
    time.sleep(0.5)
    os.system("python init_menu.py")
