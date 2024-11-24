import os

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_screen()
    print("Odd or Even Number Determiner\n\n")

    try: 
        num = int(input("Enter a Number: "))

        if num % 2 == 0:
            clear_screen()
            print(f"The number you entered which is {num} is an even number.\n\n")
            
        elif num % 2 == 1:
            clear_screen()
            print(f"The number you entered which is {num} is an odd number.\n\n")
            
    except ValueError:
        clear_screen()
        print("That ain't it, chief.\n\n")
     
    loopback = input("Would you like to try another? [Yes] or [No]: ")
    
    if loopback == "Yes" or loopback == "yes":
        main()
    
    else:
        clear_screen()
        print("Okay, have a great day! :)\n\n\n")
        exit()
        
main()