def bubble_sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
                # a_list[j], a_list[j+1] = a_list[j+1], a_list[j]  # This is the same as the above 3 lines
    return a_list



def bubble_sort_short(a_list):
    for i in range(len(a_list)-1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                exchanges = True
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        if not exchanges:
            break
    return a_list


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(a_list))
# temp = a_list[0]
# print(temp, a_list[0])
# a_list[0] = a_list[1]
# print(temp, a_list[0])
# a_list[1] = temp
# print(temp, a_list[1])
# bubble_sort(a_list)
# print(a_list)