###################################
#---FP2-F01 Reading Files
#---Reid A. Martin
###################################

import time
import random

b_or_nb = ["bones", "no bones"]
bones_days = []
no_bones_days = []
week_days = []

def read_all():
    file = open('weekdays.txt', 'r')
    every_of_the_week = file.read()
    print(every_of_the_week)
    file.close()
    
def pick_day():
    done = False
    file = open('weekdays.txt', 'r')
    week = file.read()
    week_days = week.splitlines()
   # print(week_days)
    while done == False:
        day = input("Which day do you want to predict?\n>").lower()
        #answer = week_days.get(day) Ya... it took graden and i a while...... when we tried it... this line seems to be the thing holding it from having a breakdown and im not going to test it without it...
        if day in week_days:
            if day in bones_days:
                print(day, "is a bones day!")
                done = True
                file.close()
            elif day in no_bones_days:
                print("Sadly", day, "is a no bones day.")
                done = True
                file.close()
            else:
                print("Let's see...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                bones = random.choice(b_or_nb)
                print("It appears that", day, "is a", bones, "day")
                if bones == "no bones":
                    no_bones_days.append(day)
                elif bones == "bones":
                    bones_days.append(day)
                file.close()
                done = True
        else:
            print("That is not an option")
        
def main():
    finished = False
    #another = False
    print("Welcome to Noodle the Pug's Bones or No Bones Day Predictor\n>Note: Not as accurate as the actual Noodle")
    time.sleep(2)
    print("Here is what days you can predict...")
    time.sleep(1)
    read_all()
    while finished == False:
        another = False
        pick_day()
        while another == False:
            fin = input("Would you like to predict another day?\n>" ).lower()
            if fin == "y" or fin == "yes":
                print("Alrighty!")
                time.sleep(2)
                another = True
            elif fin == "n" or fin == "no":
                print("Okay... Have a good day!")
                another = True
                finished = True
            else:
                print("That's not an option")
                
                

#pick_day()
main()