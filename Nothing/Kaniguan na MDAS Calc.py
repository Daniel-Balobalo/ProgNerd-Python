print("\nKaniguan na MDAS Calc ./.\n")

a = int(input("First Integer: "))
b = int(input("Second Integer: "))
op = input("What Operator [+][-][*][/]: ")

add = a + b
sub = a - b
mul = a * b
div = a / b

if op == "+":
    print(f"\nThe sum of {a} and {b} is {add}.\n")
    
elif op == "-":
    print(f"\nThe difference of {a} and {b} is {sub}.\n")
    
elif op == "*":
    print(f"\nThe product of {a} and {b} is {mul}.\n")
    
elif op == "/":
    print(f"\nThe quotient of {a} and {b} is {div}.\n")
    
print("\nOkay na na potangina ka?\n")

