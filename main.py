from threading import Thread, Lock
from time import sleep
import requests
import getip

from termcolor import colored
import os

iplist = getip.ip_list
os.system("cls")
#region ASCII LOGO
def printlogo():
    print(colored("       d8888 8888888b.  8888888b. ", "blue"), end="")
    print('        .d8888b.  888    888 8888888888  .d8888b.  888    d8P  ')
    print(colored("      d88888 888   Y88b 888   Y88b", "blue"), end="")
    print('       d88P  Y88b 888    888 888        d88P  Y88b 888   d8P   ')
    print(colored("     d88P888 888    888 888    888", "blue"), end="")
    print('       888    888 888    888 888        888    888 888  d8P    ')
    print(colored("    d88P 888 888   d88P 888   d88P", "blue"), end="")
    print('       888        8888888888 8888888    888        888d88K     ')
    print(colored('   d88P  888 8888888P"  8888888P" ', "blue"), end="")
    print('       888        888    888 888        888        8888888b    ')
    print(colored("  d88P   888 888 T88b   888       ", "blue"), end="")
    print('       888    888 888    888 888        888    888 888  Y88b   ')
    print(colored(" d8888888888 888  T88b  888       ", "blue"), end="")
    print('       Y88b  d88P 888    888 888        Y88b  d88P 888   Y88b  ')
    print(colored('d88P     888 888   T88b 888       ', "blue"), end="")
    print('        "Y8888P"  888    888 8888888888  "Y8888P"  888    Y88b ')
    print("")

#endregion
def check_ip(ip,lock_state):
    sleep(1)
    try:
        response = requests.get("http://" + ip)
        with lock_state:
            print(ip + " responds with " + str(response), flush=True)
    except OSError:
        with lock_state:
            print(ip + " does not respond", flush=True)
printlogo()
option = input("Would you like to scan(Y/N)?")
if option == "Y" or option == 'y':
    os.system("cls")
    printlogo()
    lock = Lock()
    threads = [Thread(target=check_ip, args=(ip,lock)) for ip in iplist]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
elif option == "N" or option == "n":
    exit()
else:
    printlogo()

    print("\n???")
    sleep(2)
    exit()