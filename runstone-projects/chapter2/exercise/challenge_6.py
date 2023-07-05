from timeit import Timer

# Function to measure the time taken to access an element at a given index
def measure_access_time(lst, index):
    element = lst[index]



list_sizes = [1000, 10000, 100000]
for size in list_sizes:
    lst = list(range(size))
    t1 = Timer(f"measure_access_time({lst}, 0)", "from __main__ import measure_access_time")
    print(f"first: {t1.timeit(number=1000):15.3f} milliseconds")
    t2 = Timer(f"measure_access_time({lst}, -1)", "from __main__ import measure_access_time")
    print(f"last: {t2.timeit(number=1000):16.3f} milliseconds")
    t3 = Timer(f"measure_access_time({lst}, {size//2})", "from __main__ import measure_access_time")
    print(f"middle: {t3.timeit(number=1000):14.3f} milliseconds")

