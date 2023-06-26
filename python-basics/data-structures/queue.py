# Implement Queue with list
class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    

    def size(self):
        return len(self.queue)
                               
my_queue = Queue()

# Push elements onto the stack
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Pop an element from the stack
print(my_queue.dequeue())  # Output: 30

# Peek the top element of the stack
print(my_queue.peek())  # Output: 20

# Check if the stack is empty
print(my_queue.is_empty())  # Output: False

# Get the size of the stack
print(my_queue.size())  # Output: 2)
