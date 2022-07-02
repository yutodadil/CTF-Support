import os
import random
import time
import getpass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

inp1 = getpass.getpass("Welcome to Setup.py!!\nEnter to continue") # 文字入力できるのはダサいから入力しても画面に出ないようにした。
inp2 = input("Start Setup? Y/n\n ->")
if inp2 == "Y" or inp2 == "y" or inp2 == "yes" or inp2 == "Yes" or inp2 == "YES":
            clear()
            print("Please Root Access.")
            os.system("sudo -i")
            clear()
            print("Start Setup...")
            os.system("apt update -y;apt upgrade -y;apt install nodejs npm git python3-pip -y") # apt update -y;apt upgradeは一緒にやるとErrorが出る場合があるのでこのように別々にしましょう。
            os.system("logout")
            inp3 = getpass.getpass("Done, Press Enter to Exit")
            print("Finish!! Cya")
            time.sleep(3)
            clear()
            os._exit(1)
elif inp2 == "N" or inp2 == "n" or inp2 == "no" or inp2 == "No" or inp2 == "NO":
            clear()
            print("Ok...\nBye.")
            time.sleep(3)
            clear()
            os._exit(1)
