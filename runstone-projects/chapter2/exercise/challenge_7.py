from timeit import Timer

# Function to measure the time taken to get an item from a dictionary
def measure_get_time(dictionary, key):
    value = dictionary.get(key)

# Function to measure the time taken to set an item in a dictionary
def measure_set_time(dictionary, key, value):
    dictionary[key] = value


dict_sizes = [1000, 10000, 100000]  # Varying dictionary sizes

for size in dict_sizes:
    dictionary = {i: i for i in range(size)}  # Create a dictionary with the specified size
    # Measure the time taken to get an item
    get_time = Timer(f"measure_get_time({dictionary}, 0)", "from __main__ import measure_get_time")
    print(f"Dictionary size: {size}, Get time: {get_time.timeit(number=1000):5.4f} seconds")
    # Measure the time taken to set an item
    set_time = Timer(f"measure_set_time({dictionary}, {size}, {size})", "from __main__ import measure_set_time")
    print(f"Dictionary size: {size}, Set time: {set_time.timeit(number=1000):5.4f} seconds")
