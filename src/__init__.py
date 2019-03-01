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

#otpy v0.0.5_b2
#changelog:
## changelog will be updated with 0.1 release
################
# KNOWN ISSUES #
################
## ISSUE NUMBER | 001
## DESCRIPTION | there is a loop in HitTheTrail.exit() that brings you back to Store.checkout()
## REASON | caused by improperly formatted if/else statement in Store.checkout(), issue resolved
## BUGFIX STATUS | FIXED 3.1.19
## FIXED BY | adding a sys.exit() to the end of HitTheTrail.exit(), and fixing Store.checkout if/else statement
## BUGFIX DEV | thatswhereurwrongkiddo


ver = "0.0.5_b2"
title = "otpy v{0}".format(ver)

#otpy is a simulator of the popular 1974 game "The Oregon Trail",
#developed by Don Rawitsch, Bill Heinemann, and Paul Dillenberger and
#published by the Minnesota Educational Computing Consortium (MECC).
