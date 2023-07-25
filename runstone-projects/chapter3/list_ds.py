class Node():
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data
    
    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next
    
    def set_next(self, node_next):
        self._next = node_next


    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)
    
# UnorderedList
class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current

        if current is None:
            raise ValueError(f"{item} is not on the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        
    def append(self, item):
        temp = Node(item)
        current = self.head
        while current is not None:
            if current.next is None:
                current.next = temp
            current = current.next
        current = temp



# append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.

# index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

# insert(pos, item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.

# pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

# pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.

    


