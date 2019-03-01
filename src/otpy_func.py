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
    print(resetc_wb)
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
from sql_names import mm1, mm2, mm3, mm4, mm5, mm6
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

months_with_31 = [3, 5, 7, 8, 10, 12]
months_with_30 = [4, 6, 9, 11]
date_c = [3, 1, 1856]

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
        elif choice.lower() == "food":
            Store.buy_food()
        elif choice.lower() == "ammo":
            Store.buy_ammo()
        elif choice.lower() == "spare parts":
            Store.buy_parts()
        elif choice.lower() == "checkout":
            Store.checkout()
        else:
            GameMods.unrecognized()
            Store.buy()
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
        global money
        total = oxen + food + ammo_price + spare_parts_price
        print(bgc_wb + txtc_wb + "Your total bill is: {0}".format(total))
        pay_now = input("Do you wish to pay now? (yes/no): ")
        if total > money:
            clearscreen()
            print(bgc_wb + txtc_wb + "Sorry, you do not have enough funds for this purchase")
            input("Press ENTER to continue...")
            pay_now = "no"
        if pay_now.lower() == "yes":
            #global money
            money = money - total
            print(resetc_wb)
            #HitTheTrail.menu()
        elif pay_now.lower() == "no":
            print(resetc_wb)
            clearscreen()
            Store.buy()
        else:
            GameMods.unrecognized()
            print(resetc_wb)
            clearscreen()
            Store.checkout()
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
2. Check supplies
3. Hunt
4. Rest
5. Exit
""".format(miles_t, money, r_date))
        if miles_t < 2000:
            p_choice = input("What would you like to do?: ")
            if int(p_choice) == 1:
                miles_t = miles_t + 10
                if date_c[0] in months_with_31 and int(date_c[1]) < 31:
                    date_c[1] = int(date_c[1]) + 1
                    HitTheTrail.menu()
                elif date_c[0] in months_with_31 and int(date_c[1]) >= 31:
                    date_c[0] = int(date_c[0]) + 1
                    date_c[1] = 1
                    HitTheTrail.menu()
                if date_c[0] in months_with_30 and int(date_c[1]) < 30:
                    date_c[1] = int(date_c[1]) + 1
                    HitTheTrail.menu()
                elif date_c[0] in months_with_30 and int(date_c[1]) >= 30:
                    date_c[0] = int(date_c[0]) + 1
                    date_c[1] = 1
                    HitTheTrail.menu()
            elif int(p_choice) == 2:
                HitTheTrail.supplies()
            elif int(p_choice) == 3:
                TrailHunting.main()
            elif int(p_choice) == 4:
                HitTheTrail.rest()
            elif int(p_choice) == 5:
                HitTheTrail.exit()
            else:
                GameMods.unrecognized()
                HitTheTrail.menu()
        else:
            HitTheTrail.OG_check()
    def supplies():
        clearscreen()
        global food_pounds
        global money
        global ammo
        global yokes
        global spare_parts
        oxen_count = int(yokes) * 2
        print(txtc_wb + bgc_wb + """
Your Supplies:
Food (lbs.): {0}
Money: {1}
Ammunition: {2}
Oxen: {3}
Boxes of Spare Parts: {4}
        """.format(food_pounds, money, ammo, oxen_count, spare_parts))
        input("Press ENTER to return to menu...")
        HitTheTrail.menu()
    def rest():
        HitTheTrail.notcoded()
    def exit():
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "Thanks for playing!")
        print("Check out the source code at:")
        print("https://github.com/thatswhereurwrongkiddo/otpy")
        input("Press ENTER to continue...")
        import sys
        sys.exit()
    def OG_check():
        if miles_t >= 2000:
            print("You made it to Oregon! Woo-Hoo!")
            input("Press ENTER to continue...")
            HitTheTrail.exit()
        else:
            pass
    def notcoded():
        print(resetc_wb)
        clearscreen()
        print("""
#####################################################
##                      ERROR                      ##
##                FEATURE NOT CODED                ##
##                                                 ##
##                     NOTICE:                     ##
##                                                 ##
##    THIS ERROR SHOULD ONLY EXIST IN TEST CODE    ##
#####################################################
        """)
        print("")
        print("OK, so, you found a feature I haven't coded yet.")
        print("")
        print("""If you see this message in master branch code (NOT testing/alpha-testing branch),
please write a post in the issues tab on the otpy GitHub page, with the attempted feature that gave
you the message and the version of otpy you are using""")
        print("")
        print("Otherwise, I'll probably implement this feature in anywhere from an hour to a week.")
        print("")
        input("Press ENTER to continue...")
        HitTheTrail.menu()
class TrailHunting:
    def main():
        clearscreen()
        if ammo <= 0:
            print(txtc_wb + bgc_wb + "Sorry partner, you don't have enough ammo to go hunting.")
            input("Press ENTER to return to menu...")
            HitTheTrail.menu()
        else:
            print(txtc_wb + bgc_wb + "Time to go hunting out in the wild!")
            print("You grab your rifle and set out in to the forest")
            print("")
            hunt_path = input("Do you take the *darker* path or the *lighter* path?: ")
            if hunt_path == "darker":
                TrailHunting.darker()
            elif hunt_path == "lighter":
                TrailHunting.lighter()
            else:
                GameMods.unrecognized()
                TrailHunting.main()
    def darker():
        global food_pounds
        global ammo
        global date_c
        print("You walk through a dimly lit forest path you can barely see.")
        print("You barely see a deer in the distance and aim to shoot at it.")
        shoot = input("Type 'shoot' to shoot: ")
        if shoot.lower() == "shoot":
            ammo = ammo - 1
            print("You miss and hit a tree.")
            print("")
            print("You decide to go back to the wagon and try again another day but you lose your way")
            print("(1 day lost)")
            input("Press ENTER to continue...")
            date_c[1] = int(date_c[1]) + 1
            HitTheTrail.menu()
        else:
            GameMods.unrecognized()
            TrailHunting.darker()
    def lighter():
        global food_pounds
        global ammo
        global date_c
        print("You decide to take the lighter path, as that obviously makes more sense.")
        print("You see a giant bear in the distance, and you pull out your rifle to shoot it.")
        shoot = input("Type 'shoot' to shoot: ")
        if shoot.lower() == "shoot":
            ammo = ammo - 1
            print("You hit it! The bear goes down, and now you have an extra 100 lbs. of food!")
            input("Press ENTER to continue...")
            food_pounds = food_pounds + 100
            HitTheTrail.menu()
        else:
            GameMods.unrecognized()
            TrailHunting.lighter()
