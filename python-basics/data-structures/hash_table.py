class HashTable:
    def __init__(self):
        self.table = {}

    
    def insert(self, key, value):
        self.table[key] = value

    def delete(self, key):
        if key in self.table:
            del self.table[key]
        else:
            raise KeyError(f"Key '{key}' not found in table")
        
    def search(self, key):
        if key in self.table:
            return self.table[key]
        else:
            raise KeyError(f"Key '{key}' not found in table")
        
    def contains(self, key):
        return key in self.table
        

# Create a new hash table
my_table = HashTable()

# Insert key-value pairs into the hash table
my_table.insert("apple", 5)
my_table.insert("banana", 10)
my_table.insert("orange", 7)

# Search for a value using a key
print(my_table.search("banana"))  # Output: 10

# Check if a key exists in the hash table
print(my_table.contains("apple"))  # Output: True
print(my_table.contains("grape"))  # Output: False

# Delete a key-value pair from the hash table
my_table.delete("orange")

# Attempt to access a deleted key
# This will raise a KeyError
print(my_table.search("orange"))