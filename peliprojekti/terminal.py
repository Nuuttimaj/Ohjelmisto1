import time
from colours import värit
from pelaaja import user_name


time.sleep(2)
print(f'''{värit.BOLD}{värit.OKGREEN}
        The Organization
        
        Authorized use only

        You may be subjected to bodily harm or death, if you proceed unauthorized
        
        ''')

time.sleep(3)
while True:
    proceed=input(f'''{värit.BOLD}{värit.OKGREEN}
            Press enter to proceed?
            ''')

    if proceed == "":
        break

while True:
    password=input(f'''{värit.BOLD}{värit.OKGREEN}
            Password?
            ''')

    if password == "Password1":
        break
    print(f"{värit.ENDC}{user_name}: Let's try the usual one, maybe Password1")


while True:
    sf_input=input(f'''{värit.BOLD}{värit.OKGREEN}
            Safe house 87
            > Personnel
            > Latest Log
            > Exit

            Where do you wish to proceed
            ''')

    if sf_input == "Personnel":
        time.sleep(1)
        print(f'''{värit.BOLD}{värit.OKGREEN}
        Doctor Collins, Medical supervisor
        General Fields, Director of security
        Classified, Classified
        ''')
        time.sleep(1)
    if sf_input =="Latest Log":
        time.sleep(1)
        print(f'''{värit.BOLD}{värit.OKGREEN}
        Doctor Collins, Medical Supervisor

        The Plan has started, their wake up time has been set.

        We are moving to the safe room to observe and execute the final step of the plan if needed.

        All hail The Organization 
        ''')
        time.sleep(3)
        print(f"{värit.ENDC}{user_name}: What plan?")
    if sf_input =="Exit":
        break







