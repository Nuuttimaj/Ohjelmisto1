#Funktioon tarvittavat importit
import time
import random
import pelaaja
import machine
import os

#Act 3 Combat kokonaisuudessaan
def combat():
    while True:
        print("The machine has engaged you in combat, what do you want to do?")
        time.sleep(1)
        hit=input("Critical Hit(0-50HP)or Normal Hit(20HP)? ").lower()
        if hit == "critical hit":
            machine.masiina.Machine_hp_muutos(random.randint(0,50))
            if machine.masiina.hp <=0:
                print("The machine has been destroyed")
                break
            print(f"The Machine HP: {machine.masiina.hp}")
            time.sleep(1)
            print("You have given the machine a chance to hit you")
            pelaaja.user.hp_muutos(random.randint(0,50))
            if pelaaja.user.hp <=0:
                os.system('say "The plan has been completed, there are no more future for mankind"')
                time.sleep(1)
                print("You have been killed!")
                time.sleep(1)
                print("We thank you for playing Safe House 87")
                quit()
            time.sleep(1)
            print(f"Your HP:{pelaaja.user.hp}")
        else: 
            machine.masiina.Machine_hp_muutos(20)
            if machine.masiina.hp <=0:
                print("The machine has been destroyed")
                break
            print(f"The Machine HP: {machine.masiina.hp}")
            time.sleep(1)
            print("You have given the machine a chance to hit you")
            pelaaja.user.hp_muutos(20)
            if pelaaja.user.hp <=0:
                os.system('say "The plan has been completed, there are no more future for mankind"')
                time.sleep(1)
                print("You have been killed!")
                time.sleep(1)
                print("We thank you for playing Safe House 87")
                quit()
            time.sleep(1)
            print(f"Your HP:{pelaaja.user.hp}")