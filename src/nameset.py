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

#nameset.py
#set up names for your wagon party members

from otpy_func_premain import clearscreen, vernotice
from color_storage import txtc_wb, bgc_wb, resetc_wb
import sqlite3 as sql

clearscreen()

print(txtc_wb + bgc_wb + "Type the names of the members of your wagon party:")
print("                                                  ")
mm1 = input("1 (You): ")
mm2 = input("2: ")
mm3 = input("3: ")
mm4 = input("4: ")
mm5 = input("5: ")
mm6 = input("6: ")
print(resetc_wb)

import os
os.system("cd .. && mkdir tmp")
conn = sql.connect("../tmp/nameset.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE `otpy_names`(
`num` INTEGER,
`name` TEXT
);''')
cursor.execute('INSERT INTO otpy_names (num, name) VALUES (1, "{0}"),(2, "{1}"),(3, "{2}"),(4, "{3}"),(5, "{4}"),(6, "{5}")'.format(mm1,mm2,mm3,mm4,mm5,mm6))
conn.commit()

os.system("python intro.py")
