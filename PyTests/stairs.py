import os

def clear():
    if os.name == 'nt':
        os.system('cls')
        
    else:
        os.system("clear")
        

import time
        
def loading():
    anime = "/-\|\\"
    for _ in range(3):
        for char in anime:
            print(f"\rLoading... {char}", end="")
            time.sleep(0.1)
            

def clearing():
    animation = "/-\|\\"
    for _ in range(4):
        for chari in animation:
            print(f"\rClearing the Screen... {chari}", end="")
            time.sleep(0.1)
            

def main():
    try:
        clear()
        stairs = int (input("Enter how many stairs: ")) 
        # 146 steps is the limit that the terminal can cleanly view, btw.
        print()
        loading()
        clear()
        print(f"{stairs} stairs: ")
        # Using nested for loops to print the asterisk stairs
        for i in range(stairs + 1):
            for j in range(i):
                print("*", end="")
            print()     # Move to the next line after each row
    except ValueError:
        clear()
        print("Invalid Input! Try again.\n")
        
    repeat = input("\nWould you like to try another? [Yes] [No]: ")
    if repeat == "Yes" or repeat == "yes":
        print()
        clearing()
        main()
        
    else:
        print()
        clearing()
        clear()
        print("Bye!\n\n")
        exit()
        
main()