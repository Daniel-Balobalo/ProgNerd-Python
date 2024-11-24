import os
import time

amount = 20000.00  # Declare amount outside the withdrawal() function

def clear_screen():
    if os.name == "nt":
        os.system("cls")  
    else:
        os.system("clear")
        
def processing_animation():
    animation = "-\|/"
    for _ in range(10):
        for char in animation:
            print(f"\rProcessing your withdrawal... {char}", end="")
            time.sleep(0.1)
    print()
    
    
def withdrawal():
    global amount  # Use the global amount variable

    while True:
        try:
            clear_screen()
            withdraw = float(input("Enter the Amount of Withdrawal: "))
            clear_screen()
            processing_animation()

            if withdraw > amount:
                print("Insufficient funds!")
                time.sleep(2)
                continue

            balance = round(amount - withdraw, 2)
            amount = balance  # Update the global amount variable with the new balance

            clear_screen()
            print(f"Your money withdrawal with the amount of {withdraw} is successful!")

        except ValueError:
            clear_screen()
            print("Invalid Input! Only accepts numbers.\n\n")

        withd_again = input("\n\nWould you like to withdraw again? Yes [Y] or No [N]: ")
        if withd_again.lower() == "y":
            continue  # Continue the withdrawal process
        else:
            account()
            
            
            
            
def balance_inquiry(balance):
    clear_screen()
    
    print(f"Your account's balance is {balance}.\n\n")
    
    exit_option = input('Press "E" to Exit this Balance Inquiry Menu: ')
    if exit_option.lower() == 'e':
        account()
    else:
        balance_inquiry(balance)  # Pass the balance argument when calling balance_inquiry() again



 
def account():
    global amount  # Declare 'amount' as global since it's used in the functions

    clear_screen()
    print("Withdrawal [W]")
    print("Balance Inquiry [B]")
    print("Exit [E]")
    
    option = input("\nEnter Option: ")
    
    if option == "W" or option == "w":
        withdrawal()
        
    elif option == "B" or option == "b":
        balance_inquiry(amount)  # Pass the 'amount' variable to balance_inquiry
        
    elif option == "E" or option == "e":
        main()
    
    else:
        print("Invalid Input! Only allowed input are [W], [B], and [E].")
        account()

    
    
    
    
    
def account_validation():
    PIN = input("Enter your 6 digit PIN: ")
    
    # PIN Code is 051501
    if PIN == "051501":
        account()
        
    else:
        print("Invalid PIN.")
        account_validation()
        
    

    
def main():
    
    clear_screen()
    print("""             ########################################################
             #  BBBBBB          AAA       NNNNNN   NN   KKK   KKK   #
             #  BBB   BBB     AAA AAA     NNN NNN  NN   KKK  KKK    #
             #  BBB  BBB     AAA   AAA    NNN  NNNNNN   KKK KKK     #
             #  BBB BBB      AAAAAAAAA    NNN   NNNNN   KKK  KKK    #
             #  BBB   BBB    AAA   AAA    NNN    NNNN   KKK   KKK   #
             #  BBB BBB      AAA   AAA    NNN     NNN   KKK    KKK  #
             # ######################################################""")

    print("\n")
    print("\n(Type 'Exit' to exit the application)\n")

    ATM = input("Press 'E' to Enter your Card: ")
    
    
    if ATM == "E" or ATM == "e":
        account_validation()
        
    elif ATM == "Exit" or ATM == "exit":
        clear_screen()
        print("Thank you for using this prototype application. :)\n\n")
        exit()
        
    else: 
        main()
        
        
main()
    