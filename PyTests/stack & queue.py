# Stack
stack = []
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack")
print(stack)

print("\nElements destacked from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after removing elements: ")
print(stack)


# Queue
queue = []
queue.append("a")
queue.append("b")
queue.append("c")

print('\n\nInital queue')
print(queue)

print('\nElements dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nQueue after removing elements')
print(queue)