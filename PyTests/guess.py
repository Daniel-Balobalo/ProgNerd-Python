import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
        
    else:
        os.system("clear")



import time

def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(f"\rLoading... {char}", end="")
            time.sleep(0.1)  # Adjust the delay as needed
    print("\nLoading complete!\n")


import random

def main():

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    clear_screen()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = 0
    while True:
        try: 
            guess = int(input("\n\nTake a guess: "))
            attempts += 1
            
            if guess < random_number:
                clear_screen()
                print(f"{guess} is too low! Try again.")
                
            elif guess > random_number:
                clear_screen()
                print(f"{guess} is too high! Try again.")
                
            else:
                clear_screen()
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        
        except ValueError:
            clear_screen()
            print("Invalid input. Enter a number, bruv. Don't be trippin'.")
        
    repeat = input("\n\nWould you like to restart the game? [Yes][No]: ")
    
    if repeat == "Yes" or repeat == "yes":
        print("\n\n")
        loading_animation()
        clear_screen()
        main()
        
    else: 
        print("\n\n")
        loading_animation()
        clear_screen()
        print("Bye! :)\n\n")
        exit()
        
main()