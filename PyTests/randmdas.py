import os
import random

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear_screen()
    print("""▄▄▄   ▄▄▄·  ▐ ▄ ·▄▄▄▄        • ▌ ▄ ·.     • ▌ ▄ ·. ·▄▄▄▄   ▄▄▄· .▄▄ ·      ▄▄▄·▄▄▄        ▄▄▄▄· 
▀▄ █·▐█ ▀█ •█▌▐███▪ ██ ▪     ·██ ▐███▪    ·██ ▐███▪██▪ ██ ▐█ ▀█ ▐█ ▀.     ▐█ ▄█▀▄ █·▪     ▐█ ▀█▪
▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▐█· ▐█▌ ▄█▀▄ ▐█ ▌▐▌▐█·    ▐█ ▌▐▌▐█·▐█· ▐█▌▄█▀▀█ ▄▀▀▀█▄     ██▀·▐▀▀▄  ▄█▀▄ ▐█▀▀█▄
▐█•█▌▐█ ▪▐▌██▐█▌██. ██ ▐█▌.▐▌██ ██▌▐█▌    ██ ██▌▐█▌██. ██ ▐█ ▪▐▌▐█▄▪▐█    ▐█▪·•▐█•█▌▐█▌.▐▌██▄▪▐█
.▀  ▀ ▀  ▀ ▀▀ █▪▀▀▀▀▀•  ▀█▄▀▪▀▀  █▪▀▀▀    ▀▀  █▪▀▀▀▀▀▀▀▀•  ▀  ▀  ▀▀▀▀     .▀   .▀  ▀ ▀█▄▀▪·▀▀▀▀ """)
    print("\nHi! What's your name?")
    name = input("\n\nEnter your Name: ").strip().title()

    def ready():
        clear_screen()
        print(f"Hi, {name}! Hope you're having an awesome life!\n")
        print(f"C'mon, {name}! Let's play this game.\n")
        print("""Instruction: You will be presented with random MDAS problems. When the game starts, you'll have 3 lives. Each time you input a wrong answer to a problem, you lose 1 life. When you get 5 correct answers consecutively, 1 life will be added to your "livestock".\n""")
        answer = input("Are you In or Out?: [I] or [O]: ")

        if answer.lower() == "i":
            game()
        else:
            clear_screen()
            print("Aight, comeback when you're in for it. :)\n")
            exit()

    def game():
        clear_screen()
        lives = 3
        correct_answers = 0
        operators = ['+', '-', '*', '/']

        while lives > 0:
            num1 = random.randint(1, 999)
            num2 = random.randint(1, 999)
            randop = random.choice(operators)
            print(f"Lives Remaining: {lives}")

            # Display the problem
            print(f"What is {num1} {randop} {num2}?")

            try:
                user_input = input("Your answer: ").replace(',', '')  # Remove commas from user input
                if randop == '/':
                    user_answer = round(float(user_input), 2)
                else:
                    user_answer = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Calculate the correct answer
            if randop == '+':
                correct_answer = num1 + num2
            elif randop == '-':
                correct_answer = num1 - num2
            elif randop == '*':
                correct_answer = num1 * num2
            elif randop == '/':
                if num2 != 0:
                    correct_answer = round(num1 / num2, 2)
                else:
                    print("Cannot divide by zero. Let's give you something else.")
                    continue

            # Check user's answer
            if user_answer == correct_answer:
                clear_screen()
                print("Correct!")
                correct_answers += 1
                if correct_answers % 5 == 0:
                    lives += 1
                    print(f"Congratulations, {name}! You've got 5 in a row. You've earned an extra life!")
            else:
                clear_screen()
                print("Incorrect answer!")
                lives -= 1
                correct_answers = 0

        clear_screen()
        print("Game Over!")
        formatted_score = '{:,}'.format(correct_answers * 5)  # Format the score with commas
        print(f"Hey, {name}, you scored {formatted_score} points!")

    ready()

main()
