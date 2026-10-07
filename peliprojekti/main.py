#Importit
import time
from pelaaja import user


#Main menu
import menu



#Intro
time.sleep(3)
print("Waking up sequence started")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(f"Good morning {user.nimi}!")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("You have been sleeping for quite some time.")
time.sleep(2)
print("It is the year 2088")
time.sleep(3)
print(f"You are now {user.ikä + 62} years old ")
time.sleep(2)
print("Due to the advancements made by The Organization, you are free to leave.")
time.sleep(1)
print("We thank you for your stay and wish you a joyful life.")
time.sleep(3)


#Act 1
print(f"{user.nimi}: I need to get out!")
print("You see a staircase covered in frost.")
act1_staircase = input("Press enter to continue: ")
if act1_staircase == "":
    print(f"{user.nimi}: Shakey")
print(f"{user.nimi}: What happened")


