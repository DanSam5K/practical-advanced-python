class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return 

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next= current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print("True")
                return True
            current = current.next
        print("False")
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)
                
# Creat a new LinkedList
my_list = LinkedList()
my_list.print_list() # Output: None

# Append elements ot the my_list
my_list.append(10)
my_list.append(20)

my_list.print_list() # Output: 10 -> 20 -> None

# Prepend to my_list
my_list.prepend(2)
my_list.print_list() # Output: 2 -> 10 -> 20 -> None

# Search data
my_list.search(115) # False
my_list.search(10) # True