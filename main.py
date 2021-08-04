from colorama import Fore, Back, Style
import time
import subprocess
import requests
import os


hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('pastebin link') 

print(Fore.YELLOW + "Authentication", "|", "Checking license...")
print(Style.RESET_ALL)

try:
    if hwid in r.text:
        pass
    else:
        print(Fore.RED + "Authentication", "|", "HWID Not found.")
        time.sleep(5)
        os._exit()
except:
    time.sleep(3) 
    exit()

print(Fore.GREEN + "Authentication", "|", "Succesfully authenticated.")