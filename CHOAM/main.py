import os
from menu import Menu

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_screen()

print(""" _____  _   _ _____  ___  ___  ___
/  __ \| | | |  _  |/ _ \ |  \/  |
| /  \/| |_| | | | / /_\ \| .  . |
| |    |  _  | | | |  _  || |\/| |
| \__/\| | | \ \_/ / | | || |  | |
 \____/\_| |_/\___/\_| |_/\_|  |_/
                                  
[Combine Honnete Ober Advancer Mercantiles]\n""")

main_menu = Menu()  # Create an instance of the Menu class without arguments
main_menu.present_menu()
