#!/usr/bin/env python3

## MODULES ##
import sys
import os
from termcolor import colored
import time

## FUNCTIONS ##
def prompt_sudo():
    if os.geteuid() != 0:
        print("You are not sudoer!")
        sys.exit()
def nline():
    print("\n")

prompt_sudo()
os.system('clear')

## BANNER ##
print(colored("-" * 40, 'red'))
print(colored("-" * 40, 'red'))
print(colored("-" * 8 + " NMAP AUTOMATION SCRIPT " + "-" * 8, 'red'))
print(colored("-" * 40, 'red'))
print(colored("-" * 18 + " BY " + "-" * 18, 'red'))
print(colored('''
    __             ___    _       _ _        _      __            
   /  \   __ __   | __|  | |_    | | |    __| |    /  \  __ __ __ 
  | () |  \ \ /   |__ \  | ' \   |_  _|  / _` |   | () | \ V  V / 
  _\__/   /_\_\   |___/  |_||_|   _|_|_  \__,_|   _\__/   \_/\_/  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|  
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  

''', 'green'))

## PROMPT ##
print(colored('''
1 - Stealth
2 - Stealth with NSE
3 - Agressive & Instane
4 - Common ports only (21, 22, 80, 443, 3389, 5000, 8080)
5 - Same as 1 + File output & Very Verbose
''', 'magenta'))
nline()

## SCRIPT ##
method = input(colored("Choose your method >>>: ", 'green'))
ip = input(colored("Please type your ip >>>: ", 'cyan'))

if method == "1":
    sc1 = os.system('nmap -sV -sS '+str(ip))
    print(sc1)
elif method == "2":
    sc2 = os.system('nmap -sV -sS --script vuln '+str(ip))
    print(sc2)
elif method == "3":
    sc3 = os.system('nmap -A -T5 --spoof-mac Apple '+str(ip))
    print(sc3)
elif method == "4":
    sc4 = os.system('nmap -p21,22,80,443,3389,5000,8080 -sV '+str(ip))
    print(sc4)
elif method == "5":
    sc5 = os.system('nmap -sV -sS -vv -oN Scanned.txt '+str(ip))
    print(sc5)
else:
    print(colored("Not an Option!!!", 'yellow'))
    time.sleep(1)
    print(colored("Exiting...", 'red'))
    time.sleep(2)
    sys.exit()