import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

inp1 = input("Welcome to Setup.py!!\nEnter to continue")
inp2 = input("Start Setup? Y/n")
if inp2 == "Y" or inp2 == "y" or inp2 == "yes" or inp2 == "Yes" or inp2 == "YES":
            clear()
            print("Please Root Access.")
            os.system("sudo -i")
            clear()
            print("Start Setup...")
            os.system("apt update -y;apt upgrade -y;apt install nodejs npm git python3-pip -y")
            inp3 = ("Done, Press Enter to Exit")
            print("Finish!! Cya")
            time.sleep(3)
            clear()
            os._exit(1)
