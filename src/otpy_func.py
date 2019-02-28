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

#otpy_func.py
#where everything is really stored for the main game
#main.py is just a user-facing middleman

import os
from color_storage import txtc_wb, bgc_wb, resetc_wb

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    vernotice()
def checksys():
    import platform
    from __init__ import title
    platsys = platform.system()
    if platsys == "Windows":
        os.system("title {0}".format(title))
    else:
        pass
def vernotice():
    from __init__ import ver
    #print version notice
    print("(otpy v{0} PRE-ALPHA TEST VERSION)".format(ver))
    print("""

    """)

################################################################################
## functions for main.py #######################################################
################################################################################
from sql_names import mm1
name = 0
money = 0
yokes = 0

oxen = 0
food = 0
food_pounds = 0
ammo_price = 0
ammo = 0
spare_parts_price = 0
spare_parts = 0

miles_t = 0
date_c = ["3", "1", "1856"]

class GameMods:
    def unrecognized():
        print("That is an unrecognized choice.")
        input("Please Try Again...")
class Player:
    def profile():
        global name
        global money
        name = mm1
        money = 800
    def wait_for_alpha():
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "You can play the rest of the game when the alpha version 0.1 is released!")
class Store:
    def greet():
        print("Hello there, {0}! My name is Jack, and this here's my General Store!".format(name))
        print("")
        print("I see you've got ${0} to spend, let's get down to business!".format(money))
        print("")
    def buy():
        print(txtc_wb + bgc_wb + """Your Cart:
Oxen ${0} (Yokes = {4})
Food ${1} ({7} lbs.)
Ammo ${2} (Boxes = {5})
Spare Parts ${3} (Boxes = {6})
""".format(oxen, food, ammo_price, spare_parts_price, yokes, ammo, spare_parts, food_pounds))
        choice = input("What would you like to buy? (Type 'checkout' when finished): ")
        if choice.lower() == "oxen":
            Store.buy_oxen()
        if choice.lower() == "food":
            Store.buy_food()
        if choice.lower() == "ammo":
            Store.buy_ammo()
        if choice.lower() == "spare parts":
            Store.buy_parts()
        if choice.lower() == "checkout":
            Store.checkout()
    def buy_oxen():
        print(resetc_wb)
        clearscreen()
        global yokes
        global oxen
        print(txtc_wb + bgc_wb + "A yoke is made up of two oxen")
        print("I charge $40 for one yoke")
        yokes = input("How many yokes would you like to buy?: ")
        oxen = int(yokes) * 40
        print(resetc_wb)
        clearscreen()
        Store.buy()
    def buy_food():
        print(resetc_wb)
        clearscreen()
        global food
        global food_pounds
        print(txtc_wb + bgc_wb + "I recommend 200 pounds of food for each person in your party")
        print("Since you have 5, that would be 1000 pounds")
        print("I sell food at $0.20 per pound")
        food_pounds = input("How many pounds would you like to buy?: ")
        food = int(food_pounds) * .2
        food = int(food)
        print(resetc_wb)
        clearscreen()
        Store.buy()
    def buy_ammo():
        global ammo
        global ammo_price
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "Each of my Grade A ammo boxes holds 20 bullets")
        print("and each box costs $2.")
        print("")
        ammo = input("How many boxes do you want to buy?: ")
        ammo_price = int(ammo) * 2
        print(resetc_wb)
        clearscreen()
        Store.buy()
    def buy_parts():
        global spare_parts
        global spare_parts_price
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "That wagon is bound to break on you along the way to Oregon now, son.")
        print("I strongly recommend getting at least 2 boxes of spare parts in case anything is to happen")
        print("I sell each box for $50 each")
        spare_parts = input("How many boxes would you like to buy?: ")
        spare_parts_price = int(spare_parts) * 50
        print(resetc_wb)
        clearscreen()
        Store.buy()
    def checkout():
        global oxen
        global food
        global ammo_price
        global spare_parts_price
        total = oxen + food + ammo_price + spare_parts_price
        print("Your total bill is: {0}".format(total))
        pay_now = input("Do you wish to pay now? (yes/no): ")
        if pay_now.lower() == "yes":
            global money
            money = money - total
            print(resetc_wb)
            HitTheTrail.menu()
        if pay_now.lower() == "no":
            print(resetc_wb)
            clearscreen()
            Store.buy()
class HitTheTrail:
    import random
    def menu():
        global miles_t
        global date_c
        print(resetc_wb)
        clearscreen()
        r_date = "{0}/{1}/{2}".format(date_c[0], date_c[1], date_c[2])
        print(txtc_wb + bgc_wb + """Menu:
Miles Traveled: {0}/2000 | Remaining Money: {1} | Current Date: {2}
------------
1. Travel
2. Exit
""".format(miles_t, money, r_date))
        p_choice = input("What would you like to do?: ")
        if int(p_choice) == 1:
            miles_t = miles_t + 10
            date_c[1] = int(date_c[1]) + 1
            HitTheTrail.menu()
        elif int(p_choice) == 2:
            HitTheTrail.exit()
        else:
            GameMods.unrecognized()
            HitTheTrail.menu()
    def exit():
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "Thanks for playing!")
        print("Check out the source code at:")
        print("https://github.com/thatswhereurwrongkiddo/otpy")
