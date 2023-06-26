# Stack implemntation with list
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# implementation from scratch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_2:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def get_size(self):
        return self.size


# Create a new stack
my_stack = Stack()

# Push elements onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Pop an element from the stack
print(my_stack.pop())  # Output: 30

# Peek the top element of the stack
print(my_stack.peek())  # Output: 20

# Check if the stack is empty
print(my_stack.is_empty())  # Output: False

# Get the size of the stack
print(my_stack.size())  # Output: 2