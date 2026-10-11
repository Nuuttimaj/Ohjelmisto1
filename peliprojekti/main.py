#Welcome
with open("/Users/nuuttimajoinen/Desktop/Koulu/Ohjelmisto 1/Python-harjoitukset/peliprojekti/welcome.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)



#Importit
import random
import time
import pelaaja
from pelaaja import user
import os
from colours import värit
import machine
import combat



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
os.system('say "Good morning"')
time.sleep(1)
print(".")
time.sleep(1)
print(f"{user.nimi}: What's that voice?")
time.sleep(1)
print(".")
os.system('say "You have been sleeping for quite some time."')
time.sleep(1)
print(f"{user.nimi}: Huh?")
time.sleep(1)
os.system('say "It is the year 2088"')
time.sleep(1)
os.system('say "Due to the advancements made by The Organization, you are free to leave."')
time.sleep(1)
os.system('say "We thank you for your stay and wish you a joyful life."')
time.sleep(3)


#Act 1
print(f"{user.nimi}: I need to get out!")
time.sleep(1)
print("You see a staircase covered in frost.")
act1_staircase = input("Press enter to continue: ")
if act1_staircase == "":
    print(f"{user.nimi}: Shakey")
    time.sleep(1)
print(f"{user.nimi}: What are those machines?")
time.sleep(1)
os.system('say "They are sleep pods. You just woke up from one of them"')
time.sleep(1)
print(f"{user.nimi}: What?")
time.sleep(1)
os.system('say "Yes. I said you have been sleeping for some time"')
time.sleep(1)
print(f"{user.nimi}: What is this behind my ear?")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
os.system('say "I am not authorized to tell you that information."')
time.sleep(1)
print(".")
time.sleep(1)
print(f"{user.nimi}: What's your name?")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
os.system('say "I am not authorized to tell you that information."')



#Act 2
time.sleep(1)
print("You sit down to gather your thoughts")
time.sleep(1)
print(f"{user.nimi}: What the hell has happened?")
time.sleep(1)
print("Suddenly you see a computer")
time.sleep(1)
terminal_input=input("Do you want to boot the terminal?").lower()
while True:
    if terminal_input == "yes":
        import terminal
        from terminal import vastaukset
        break


#Act 3
time.sleep(1)
if "Latest Log" in vastaukset:
    print(f"{värit.ENDC}{user.nimi}: Now tell me everything")
    time.sleep(1)
    print(f"{värit.ENDC}{user.nimi}: What plan?")
    time.sleep(1)
    print(f"{user.nimi}: Why I'm the only one awake?")
    time.sleep(1)
    os.system('say "I am not authorized to tell you that information."')
    time.sleep(1)
    print(f"{user.nimi}: Why?")
    time.sleep(1)
    os.system('say "Calm down please!"')
    time.sleep(1)
    print(f"{user.nimi}: I am calm")
    time.sleep(1)
    os.system('say "You have escalated the situation, I need to finish the plan!"')
    time.sleep(1)

#Combat
combat.combat()


#Act 4
time.sleep(3)
print(f"{värit.ENDC}{user.nimi}: What is happening, Why am I the only one awake, and what plan?")
time.sleep(1)
print(".")
time.sleep(1)
print(f"{värit.ENDC}{user.nimi}:You find a note that says root and sesame.")
time.sleep(1)
print(".")
time.sleep(1)
print(f"{user.nimi}: Weird")
time.sleep(1)
print(".")
time.sleep(1)
append= input("Do you want to add the note to your inventory? ").lower()
if append == "yes":
    pelaaja.inventaario.append("Note")
time.sleep(1)
print(".")
time.sleep(1)
print(f"{user.nimi}: Another terminal! Let's boot it")
time.sleep(1)
import final_terminal
time.sleep(1)
print(f"{värit.ENDC}{user.nimi}: That's it. I finally get out!")
time.sleep(1)
print(".")
time.sleep(1)
out = input(f"{värit.ENDC}Press enter to exit the safe house!")
if out == "":
    print("Starting exit sequence")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    print(f"{user.nimi}: What's happening?")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user.nimi}: What's that gas?")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user.nimi}: I can't breathe!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"{user.nimi}: You sons of........")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    os.system('say "The plan has been completed, there are no more future for mankind"')
    print("We thank you for playing Safe House 87")
    quit()
