import os
import time
import random

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def rolling_animation():
    animation = "(¯)_"
    for _ in range(10):
        for char in animation:
            print(f"\rDice Rolling... {char}", end="")
            time.sleep(0.1)
    print()

def main():
    clear_screen()
    print("Welcome to Dice Betting Game!\n")
    print("Instruction: There are three dices to be rolled.")
    print("That means you can only bet from numbers 1-18.")
    print("Also, you only have 2 consolation attempts after your first attempt if your entered bet is invalid.")
    print("Good luck!\n\n")
    
    
    while True:
        max_attempt = 3
        attempts = 0
        while attempts < max_attempt:
            try:
                bet = int(input("Enter your bet: "))
                print()
                
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)    
                dice3 = random.randint(1, 6)
                
                luckynumber = dice1 + dice2 + dice3
                
                attempts += 1   # Count this as an invalid input attempt for greater than 18 condition.
                if bet < luckynumber:
                    rolling_animation()
                    clear_screen()
                    print(f"Your bet: {bet}")
                    print(f"The first dice is {dice1}, the second dice is {dice2}, and the third dice is {dice3}. ")
                    print(f"The Lucky Number is {luckynumber}.")
                    print(f"I'm sorry, your bet is lower than the Lucky Number which is {luckynumber}.")
                    print()
                    print()
                    break
                    
                elif bet > 18:
                    clear_screen()
                    print("I'm sorry, but your entered bet is higher than what the three dice can only roll, which is 18.")
                    print(f"{max_attempt - attempts} remaining attempts to try again.")
                    print()
                    
                
                elif bet > luckynumber:
                    rolling_animation()
                    clear_screen()
                    print(f"Your bet: {bet}")
                    print(f"The first dice is {dice1}, the second dice is {dice2}, and the third dice is {dice3}. ")
                    print(f"The Lucky Number is {luckynumber}.")
                    print(f"I'm sorry, your bet is higher than the Lucky Number which is {luckynumber}.")
                    print()
                    print()
                    break
                    
                else:
                    rolling_animation()
                    clear_screen()
                    print(f"Your bet: {bet}")
                    print(f"The first dice is {dice1}, the second dice is {dice2}, and the third dice is {dice3}. ")
                    print(f"The Lucky Number is {luckynumber}.")
                    print(f"Congratulations! You won the lottery!.")
                    print()
                    print()
                    break
                
            except ValueError:
                attempts += 1
                if attempts < max_attempt:
                    clear_screen()
                    print(f"I'm sorry, but that's not a number. \nYou have {max_attempt - attempts} remaining attempts.")
                    print()
                else:
                    clear_screen()
                    print("You've already used all your consolation attempts.")
                    print()
                    print()
                    break
        
        again = input("Would you like to bet again? Yes[Y] or No[N]: ")
        if again.lower() == "y":
            main()
        else:
            clear_screen()
            print("Thanks for participating in this betting game. Bye! :) \n\n")
            exit()

main()

        # Updates from my previous code
"""
1. Moved the attempts increment code inside the try block to track the number of attempts correctly.

2. Added code to reset the attempts counter when the user decides to play again.

3. I added a while attempts < max_attempt loop to handle the scenario where the user 
   has two more attempts if they enter an invalid bet or a bet greater than 18.

4. Inside the except ValueError block, I added logic to check if the user has more 
   attempts left (if attempts < max_attempt) and provided the appropriate message. 
   If they have exhausted all attempts, it displays the message that they've used 
   all consolation attempts.
"""
