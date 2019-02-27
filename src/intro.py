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

#intro.py
#provides story intro

from otpy_func_premain import *
from color_storage import txtc_wb, bgc_wb, resetc_wb
from sql_names import *

clearscreen()


print(txtc_wb + bgc_wb + """Welcome to the Oregon Trail!
The year is 1847
By your side, you, {0}, have your faithful companions:
{1}
{2}
{3}
{4}
{5}""".format(mm1, mm2, mm3, mm4, mm5, mm6))
print("")
print("""Your journey to Oregon begins in Independence, MO
You started off with $1000, bought a wagon for $200, now you have $800
left to spend.
""")
input("Press ENTER to visit the General Store...")
print(resetc_wb)

import os
os.system("python main.py")
