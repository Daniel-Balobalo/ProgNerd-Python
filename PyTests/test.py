import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
        
    else:
        os.system("clear")
        
def main(): 
    fi = int(input("Enter First Integer: "))
    si = int(input("Enter Second Integer: "))
    
    op = input("""Which Operation: 
               [A] Addition
               [S] Subtraction
               [M] Multiplication
               [D] Division
               
               Enter Operation: """)
    
    

if __name__ == "__main__":
    main()