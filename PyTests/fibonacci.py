def fibonacci_sequence(n):

    fib_sequence = [0, 1]
    
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    print(fibonacci_sequence(num_terms))