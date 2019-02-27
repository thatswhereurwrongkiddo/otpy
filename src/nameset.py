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

from otpy_func import clearscreen, vernotice
from color_storage import txtc_wb, bgc_wb, resetc_wb

clearscreen()
vernotice()

members = input(txtc_wb + bgc_wb + "How many members are in your wagon party?: ")

class Members:
    def three():
        member1 = input("1 (You): ")
        member2 = input("2: ")
        member3 = input("3: ")
    def four():
        member1 = input("1 (You): ")
        member2 = input("2: ")
        member3 = input("3: ")
        member4 = input("4: ")
    def five():
        member1 = input("1 (You): ")
        member2 = input("2: ")
        member3 = input("3: ")
        member4 = input("4: ")
        member5 = input("5: ")
    def six():
        member1 = input("1 (You): ")
        member2 = input("2: ")
        member3 = input("3: ")
        member4 = input("4: ")
        member5 = input("5: ")
        member6 = input("6: ")

if members == "3":
    Members.three()
elif members == "4":
    Members.four()
elif members == "5":
    Members.five()
elif members == "6":
    Members.six()
else:
    import time
    print("Invalid Response")
    print("Try again")
    time.sleep(0.5)
    import os
    print(resetc_wb)
    os.system("python nameset.py")
