import os

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
        
        
        
import time

def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(f"\rLoading... {char}", end="")
            time.sleep(0.1)  # Adjust the delay as needed
    


def main():
    
        clear_screen()
        print("Hello there!")
        name = input("\nWhat's your name? ").strip().title()
        clear_screen()
        print(f"\nHi, {name}!\nHope you always have a great day!\n\n" )



        def calc():
            try:           
                print(f"C'mon, {name}. Let's calculate something.\n")
                num1 = int(input("Enter 1st Integer: "))
                num2 = int(input("Enter 2nd Integer: "))
                clear_screen()
                print(f"What Operation should we use for {num1} and {num2}?\n")
                op = input("""Enter an Operation:
                                [+] Addition
                                [-] Subtraction
                                [*] Multiplication
                                [/] Division
                                >>> """)

                def add_num(num1, num2):
                    sum = num1 + num2
                    return sum

                def sub_num(num1, num2):
                    dif = num1 - num2
                    return dif

                def mul_num(num1, num2):
                    pro = num1 * num2
                    return pro

                def div_num(num1, num2):
                    quo = num1 / num2
                    return quo

                sum_result = add_num(num1, num2)
                dif_result = sub_num(num1, num2)
                pro_result = mul_num(num1, num2)
                quo_result = round(div_num(num1, num2), 2)
                
                spat = str.upper(name) # --> To turn the string output "name" into uppercase

                if op == '+':
                    clear_screen()
                    print(f"\nThe Sum of {num1} and {num2} is {sum_result}.\n")
                    print("\nNice One!\n\n")

                elif op == '-':
                    clear_screen()
                    print(f"\nThe Difference of {num1} and {num2} is {dif_result}.\n")
                    print("\nNice One!\n\n")

                elif op == '*':
                    clear_screen()
                    print(f"\nThe Product of {num1} and {num2} is {pro_result}.\n")
                    print("\nNice One!\n\n")

                elif op == '/':
                    clear_screen()
                    print(f"\nThe Quotient of {num1} and {num2} is {quo_result}.\n")
                    print("\nNice One!\n\n")

                else:
                    clear_screen()
                    print(f"\nWhat the fuck is that, {spat}? That's not included in the Operation options I gave you, you dipshit!")
                    print(f"You had ONE JOB! ONE FUCKING JOB, {name}!\nYou know what, fuck you, man ./.\n\n")

            except ValueError:
                clear_screen()
                print("That's not an Integer, you MORON!\n\n")

            Repeat = input("Okay, would you like to try again? [Yes] or [No]: ").strip()
            
            if Repeat == 'yes' or Repeat == 'Yes':
                clear_screen()
                calc()
            else:
                clear_screen()
                print("Aight, bet!\n\n")
                
        calc()
        
        repeat = input("Next person or nah? [Yes] or [No]: ").strip()

        if repeat == 'yes' or repeat == 'Yes':
            print(" ")
            loading_animation()
            main()
        else:
            loading_animation()
            clear_screen()
            print("Aight, cool. Bye! :)\n\n")
            exit()

main()