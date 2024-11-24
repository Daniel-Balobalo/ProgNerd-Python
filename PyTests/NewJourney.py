#Asks the user of their name
name = input("Hi, what's up! What's your name?\n\n")

#Remove the whitespace in the string.
name = name.strip()

#Title case the string (Automatically make the initials capital).
name = name.title()

"""Or you can just combine them

For example:

name = name.strip().title()

   Or even simpler
   
name = input("Hi, what's up! What's your name?\n\n").strip().title()

"""

#Prints the user's name with greetings
print(f"\n\nHi, {name}!")
print("Hope you'll have a great day! :)\n")

#Focusing on Data Types and Processes
    
print("\n\nHello, \"friend\"!\nHow about another task?")

first_int = input("Enter First Integer: ")
second_int = input("Enter Second Integer: ")
op = input("Select Operator [+][-][*][/]: ")

sum = int(first_int) + int(second_int)
dif = int(first_int) - int(second_int)
pro = int(first_int) * int(second_int)
quo = round(float(first_int) / float(second_int), 2) #This one results in the nearest decimal point.
#quo = round(int(first_int) / int(second_int)) --> rounds off the quotient
#quo = float(first_int) / float(second_int) --> normal way of doing it

if op == "+":
    print(f"\nThe sum of {first_int} and {second_int} is {sum}.\n")
    
elif op == "-":
    print(f"\nThe difference of {first_int} and {second_int} is {dif}.\n")
    
elif op == "*":
    print(f"\nThe product of {first_int} and {second_int} is {pro}.\n")
    
elif op == "/":
    print(f"\nThe quotient of {first_int} and {second_int} is {quo}.\n")
    
else:
    print(f"\n\nInvalid Input.\n\n")
    

    