import os
import colorama
import time
import random
import json 
import string
from time import sleep
from colorama import Fore, Back, Style,init
commands = json.loads(open('commands.json').read())
def clear():
  os.system('clear' if os.name != "nt" else "cls")
def main():
  print(f"{Fore.CYAN}This is rawShell v2.0.4 (Based on Python)")
  username = "user"
  print(f"{Fore.RED}Please, run this app as Terminal   PowerShell Python. Colors are not working without it! & Hello, {username}!")
  init(True if os.system == "nt" else False)
  while 1:
    command = input(f"{Fore.CYAN}{username}@shell {Fore.RED}> {Fore.WHITE}")
    if command == "edituser":
        usernamechng = input("Please, input the new name of shell!: ")
        confirm = input(f"{Fore.RED}Are you sure? (y/n): ")
        if confirm == "y" or confirm == "yes" or confirm == "Y" or confirm == "YES" or confirm == "Yes":
            username = usernamechng
            input("Press any key to go back!")
            clear()
        else:
                print(f"{Fore.RED}Aborted.{Fore.WHITE}")
    elif input == "y" or input == "yes" or input == "Y" or input == "YES" or input == "Yes":
        sleep(0.5)
    elif command == "exit":
        exitsure = input(f"{Fore.RED}Are you sure you want to exit the application?: ")
        if exitsure.lower() == "y" or exitsure.lower() == "yes":
            print(f"{Fore.RED}Bye, {username}.. 😥")
            sleep(0.5)
            exit()
        else:
            print(f"{Fore.RED}Aborted.")
            input("Press any key to go back!")
            clear()
    elif command == "hi":
        print(f"{Fore.RED}Hi, {Fore.CYAN}{username}!")
        input("Press any key to go back!")
        clear()
    elif command == "bye":
        print(f"{Fore.RED}Bye, {Fore.CYAN}{username}.")
        input("Press any key to go back!")
        clear()
    elif command == "print":
        whattoprint = input("Please write what to print!: ")
        print(f"{Fore.RED}Shell said: %s" % whattoprint)
        input("Press any key to go back!")
        clear()
    elif command == "help":
        for key,value in commands.items():
            print(f"{key} : {value.get('command_info')} | Args: {value.get('args')}")
        input("Press any key to go back!")
        clear()
    else:
      sleep(0.5)
      print(f"{Fore.RED}Unknown command %s! Say help to see the current commands." % command)
      sleep(0.5)
if __name__ == "__main__":
  main()
  
