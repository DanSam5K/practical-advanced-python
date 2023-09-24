class Sorting:
    def __init__(self):
        pass

    def bubble_sort(self, a_list):
        for i in range(len(a_list)-1, 0, -1):
            for j in range(i):
                if a_list[j] > a_list[j+1]:
                    temp = a_list[j]
                    a_list[j] = a_list[j+1]
                    a_list[j+1] = temp
                    # a_list[j], a_list[j+1] = a_list[j+1], a_list[j]  # This is the same as the above 3 lines
        return a_list


    def bubble_sort_short(self, a_list):
        for i in range(len(a_list)-1, 0, -1):
            exchanges = False
            for j in range(i):
                if a_list[j] > a_list[j+1]:
                    exchanges = True
                    a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
            if not exchanges:
                break
        return a_list

    def selection_sort(self, a_list):
        for i, item in enumerate(a_list):
            min_index = len(a_list) - 1
            for j in range(i, len(a_list)):
                if a_list[j] < a_list[min_index]:
                    min_index = j
            if min_index != i:
                a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
        return a_list

    def insertion_sort(self, a_list):
        for i in range(1, len(a_list)):
            current_value = a_list[i]
            position = i
            while position > 0 and a_list[position-1] > current_value:
                a_list[position] = a_list[position-1]
                position -= 1
            a_list[position] = current_value
        return a_list

    def shell_sort(self, a_list):
        pass



a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_data = Sorting()
print(sort_data.bubble_sort(a_list))
print(sort_data.bubble_sort_short(a_list))
print(sort_data.selection_sort(a_list))
print(sort_data.insertion_sort(a_list))
# temp = a_list[0]
# print(temp, a_list[0])
# a_list[0] = a_list[1]
# print(temp, a_list[0])
# a_list[1] = temp
# print(temp, a_list[1])
# bubble_sort(a_list)
# print(a_list)