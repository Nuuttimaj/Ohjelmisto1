#Welcome
with open("/Users/nuuttimajoinen/Desktop/Koulu/Ohjelmisto 1/Python-harjoitukset/peliprojekti/welcome.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)



#Importit
import time
from pelaaja import user
import os
from colours import värit


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
print(f"{user.nimi}: What happened, what are those machines?")
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
print(f"{user.nimi}: What the hell has happened")
time.sleep(1)
print("Suddenly you see a computer")
time.sleep(1)
terminal_input=input("Do you want to boot the terminal?")
while True:
    if terminal_input == "Yes":
        import terminal
    else:
        print(f"{user.nimi}: Maybe I don't got time for that.")
        break

#Act 3



#Act 4
time.sleep(1)
print(f"{user.nimi}: Another terminal! Let's boot it")
time.sleep(1)
import final_terminal
time.sleep(1)
print(f"{värit.ENDC}{user.nimi}: That's it. I finally get out!")
time.sleep(1)
out = input(f"{värit.ENDC}Press enter to exit the safe house!")
if out == "":
    print("Starting exit sequence")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    print(f"{user.nimi}: What's happening?")
    time.sleep(2)
    print(f"{user.nimi}: I can't breathe!")
    time.sleep(2)
    print(f"{user.nimi}: You sons of........")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    os.system('say "The plan has been completed, they are no more the future of mankind"')
    print("We thank you for playing Safe House 87")
    quit()
