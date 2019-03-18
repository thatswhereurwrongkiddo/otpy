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

class NameChoice:
    def ncifel():
        global mm1
        mm1 = input(txtc_wb + bgc_wb + "Type your name: ")
        mm1 = mm1.capitalize()
        if mm1.lower() == "" or mm1.lower() == " ":
                print("Invalid name choice.")
                print()
                print("Names need to be at least one character long.")
                input("Press ENTER to continue...")
                clearscreen()
                NameChoice.ncifel()
        print("")
        y_n = input("You chose {0}, is that correct?: ".format(mm1))
        if y_n.lower() == "n" or y_n.lower() == "no":
            clearscreen()
            NameChoice.ncifel()
        elif y_n.lower() == "y" or y_n.lower() == "yes":
            pass
        else:
            GameMods.unrecognized()
            NameChoice.ncifel()
def intro():
    global mm1
    clearscreen()
    print(txtc_wb + bgc_wb + """Welcome to the Oregon Trail!
    The year is 1847
    You, {0}, have decided leave home in search of greener pastures in Oregon!
""".format(mm1))
    print("")
    print("""Your journey to Oregon begins in Independence, MO
    You started off with $1000, bought a wagon for $200, now you have $800
    left to spend.
    """)
    input("Press ENTER to visit the General Store...")
    print(resetc_wb)
    clearscreen()

name = 0
money = 0
yokes = 0

global mm1

mm1_health = 0
oxen = 0
food = 0
food_pounds = 0
ammo_price = 0
ammo_box = 0
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
        clearscreen()
class Player:
    def profile():
        global name
        global money
        global mm1_health
        name = mm1
        money = 800
        mm1_health = "Good"
class Store:
    def greet():
        Player.profile()
        print(txtc_wb + bgc_wb + "Hello there, {0}! My name is Jack, and this here's my General Store!".format(name))
        print("")
        print("I see you've got ${0} left to spend, let's get down to business!".format(money))
        print("")
    def buy():
        global total
        total = oxen + food + ammo_price + spare_parts_price
        print(txtc_wb + bgc_wb + """Your Cart:
Oxen: ${0} (Yokes = {4})
Food: ${1} ({7} lbs.)
Ammo: ${2} (Boxes = {5})
Spare Parts: ${3} (Boxes = {6})
Total: ${8}
""".format(oxen, food, ammo_price, spare_parts_price, yokes, ammo_box, spare_parts, food_pounds, total))
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
        print(txtc_wb + bgc_wb + "I recommend 200 pounds of food to start off your trip safely")
        print("I sell food at $0.50 per pound")
        food_pounds = input("How many pounds would you like to buy?: ")
        food = int(food_pounds) * .5
        food = int(food)
        print(resetc_wb)
        clearscreen()
        Store.buy()
    def buy_ammo():
        global ammo
        global ammo_price
        global ammo_box
        print(resetc_wb)
        clearscreen()
        print(txtc_wb + bgc_wb + "Each of my Grade A ammo boxes holds 20 bullets")
        print("and each box costs $2.")
        print("")
        ammo_box = input("How many boxes do you want to buy?: ")
        ammo_price = int(ammo_box) * 2
        ammo = int(ammo_box) * 20
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
        global total
        print(bgc_wb + txtc_wb + "Your total bill is: {0}".format(total))
        pay_now = input("Do you wish to pay now? (yes/no): ")
        if total > money:
            clearscreen()
            print(bgc_wb + txtc_wb + "Sorry, you do not have enough funds for this purchase")
            input("Press ENTER to continue...")
            pay_now = "no"
        if pay_now.lower() == "yes":
            money = money - total
            print(resetc_wb)
            global days_norest
            days_norest = 0
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
        global mm1_health
        global miles_t
        global date_c
        global days_norest
        print(resetc_wb)
        clearscreen()
        r_date = "{0}/{1}/{2}".format(date_c[0], date_c[1], date_c[2])
        if days_norest >= 6:
            print(txtc_wb + bgc_wb + "You should probably think about resting, before your health gets too low.")
        print(txtc_wb + bgc_wb + """Menu:
Miles Traveled: {0}/2000 | Remaining Money: {1} | Current Date: {2} | Health: {3}
------------
1. Travel
2. Check supplies
3. Hunt
4. Rest
5. Exit
""".format(miles_t, money, r_date, mm1_health))
        if miles_t < 2000:
            p_choice = input("What would you like to do?: ")
            if int(p_choice) == 1:
                HitTheTrail.travel()
            elif int(p_choice) == 2:
                HitTheTrail.supplies()
            elif int(p_choice) == 3:
                TrailHunting.main()
            elif int(p_choice) == 4:
                HitTheTrail.rest()
            elif int(p_choice) == 5:
                HitTheTrail.exit()
            elif int(p_choice) == 6:
                HitTheTrail.health_sys_checker()
            else:
                GameMods.unrecognized()
                HitTheTrail.menu()
        else:
            HitTheTrail.OG_check()
    def travel():
        global miles_t
        global days_norest
        HealthMonitor.start()
        days_norest = days_norest + 1
        HitTheTrail.food_management()
        miles_t = miles_t + 10
        if date_c[0] in months_with_31 and int(date_c[1]) < 31:
            date_c[1] = int(date_c[1]) + 1
            HitTheTrail.menu()
        elif date_c[0] in months_with_31 and int(date_c[1]) >= 31:
            date_c[0] = int(date_c[0]) + 1
            date_c[1] = 1
            HitTheTrail.menu()
        elif date_c[0] in months_with_30 and int(date_c[1]) < 30:
            date_c[1] = int(date_c[1]) + 1
            HitTheTrail.menu()
        elif date_c[0] in months_with_30 and int(date_c[1]) >= 30:
            date_c[0] = int(date_c[0]) + 1
            date_c[1] = 1
            HitTheTrail.menu()
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
        global days_norest
        global date_c
        if date_c[0] in months_with_31 and int(date_c[1]) < 31:
            date_c[1] = int(date_c[1]) + 2
        elif date_c[0] in months_with_31 and int(date_c[1]) >= 31:
            date_c[0] = int(date_c[0]) + 1
            date_c[1] = 2
        elif date_c[0] in months_with_30 and int(date_c[1]) < 30:
            date_c[1] = int(date_c[1]) + 2
        elif date_c[0] in months_with_30 and int(date_c[1]) >= 30:
            date_c[0] = int(date_c[0]) + 1
            date_c[1] = 2
        clearscreen()
        days_norest = 0
        print(txtc_wb + bgc_wb + "You have rested for two days.")
        input("Press ENTER to return to the menu...")
        HealthMonitor.start()
        HitTheTrail.menu()
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
    def food_management():
        global food_pounds
        food_pounds = int(food_pounds)
        if food_pounds >= 10:
            food_pounds = food_pounds - 10
        elif food_pounds == 0:
            pass
        else:
            food_pounds = food_pounds - food_pounds
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
class HealthMonitor:
    def start():
        global mm1_health_int
        mm1_health_int = 100
        HealthMonitor.rest()
    def rest():
        global mm1_health_int
        global days_norest
        if 3 < days_norest < 6:
            mm1_health_int = mm1_health_int - 20
            HealthMonitor.food()
        elif 6 <= days_norest < 11:
            mm1_health_int = mm1_health_int - 40
            HealthMonitor.food()
        elif days_norest >= 11:
            mm1_health_int = mm1_health_int - 60
            HealthMonitor.food()
        else:
            HealthMonitor.food()
    def food():
        global mm1_health_int
        global food_pounds
        if int(food_pounds) > 100:
            HealthMonitor.end()
        elif 100 > int(food_pounds) > 50:
            mm1_health_int = mm1_health_int - 10
            HealthMonitor.end()
        elif 50 > int(food_pounds) > 10:
            mm1_health_int = mm1_health_int - 20
            HealthMonitor.end()
        else:
            mm1_health_int = mm1_health_int - 30
            HealthMonitor.end()
    def end():
        global mm1_health_int
        global mm1_health
        if 100 >= mm1_health_int >= 80:
            mm1_health = "Good"
        if 79 >= mm1_health_int >= 60:
            mm1_health = "Fair"
        if 59 >= mm1_health_int >= 40:
            mm1_health = "Poor"
        if 39 >= mm1_health_int >= 0:
            mm1_health = "Very Poor"
class Calamities:
    def __init__():
        pass
