from collections import deque

def hot_potato(name_list, num):
    sim_queue = deque()

    for name in name_list:
        sim_queue.appendleft(name)

    while len(sim_queue) > 1:
        for i in range(num):
            sim_queue.appendleft(sim_queue.pop())
        sim_queue.pop()
    return sim_queue.pop()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
