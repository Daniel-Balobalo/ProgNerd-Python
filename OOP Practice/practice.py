import os
from clock import Clock

def clear_screen():
    if os.name == "nt":
        os.system("cls")
        
    else:
        os.system("clear")

clock1 = Clock(10, 00, 00, "PM")
clock2 = Clock(6, 1, 00, "AM")

clear_screen()
print("\n")
clock1.alarm()
print()
clock2.time()
print("\n")