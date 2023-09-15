#@Hashing functions for use with a hash table
def hash_str(a_str, table_size):
    return sum([(ord(c)*(i+1)) for i, c in enumerate(a_str)]) % table_size

