from colorama import Fore
import time
import webbrowser
import pytesseract
import pyautogui

def banner():
    print(Fore.BLUE+"   _______  ____________"+Fore.RED+"____  ____  ______")
    print(Fore.BLUE+"  <  / __ \/ ____/ ____"+Fore.RED+"/ __ )/ __ \/_  __/")
    print(Fore.BLUE+"  / / / / / /_  / /_"+Fore.RED+"  / __  / / / / / /   ")
    print(Fore.BLUE+" / / /_/ / __/ / __/"+Fore.RED+" / /_/ / /_/ / / /    ")
    print(Fore.BLUE+"/_/\____/_/   /_/   "+Fore.RED+"/_____/\____/ /_/    ", end="\n\n")

def getSettings():
    print(Fore.RED+"[?]"+Fore.BLUE+" MS between stroke :", end="")
    delay_rpl=float(input())
    print(Fore.RED + "[?]" + Fore.BLUE + " Anti-Cheat mode ? (Y/n) :",end="")
    rpl = str(input())
    if rpl == "Y" or rpl == "y":
        acmode_rpl=True
    else:
        acmode_rpl = False
    if acmode_rpl == False:
        print(Fore.RED + "[?]" + Fore.BLUE + " Auto open ? (Y/n) :",end="")
        rpl = str(input())
        if rpl == "Y" or rpl == "y":
            autoOpen_rpl=True
        else:
            autoOpen_rpl= False
    else :
        autoOpen_rpl = False

    return delay_rpl, acmode_rpl, autoOpen_rpl

def antiCheat(stroke_delay):
    print("not implemented yet!")

def fastFingers(stroke_delay, auto_open):
    print("not implemented yet!")

def main():
    banner()
    delay, acmode, autoOpen = getSettings()
    print(Fore.RED + "[?]" + Fore.BLUE + " Ready ? (Y/n):", end="")
    rpl = str(input())
    if rpl == "Y" or rpl == "y":
        if acmode:
            antiCheat(delay)
        else:
            fastFingers(delay, autoOpen)
    else:
        print(Fore.RED + "[?]" + Fore.BLUE + " Canceled", end="")

main()