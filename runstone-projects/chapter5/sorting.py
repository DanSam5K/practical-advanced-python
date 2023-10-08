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
        sublist_count = len(a_list) // 2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                self.gab_insertion_sort(a_list, start_position, sublist_count)
            print("After increments of size", sublist_count, "The list is", a_list)
            sublist_count = sublist_count // 2
        return a_list

    def gab_insertion_sort(self, a_list, start, gap):
        for i in range(start+gap, len(a_list), gap):
            current_value = a_list[i]
            position = i
            while position >= gap and a_list[position-gap] > current_value:
                a_list[position] = a_list[position-gap]
                position -= gap
            a_list[position] = current_value
        return a_list

    def merge_sort(self, a_list):
        print("Splitting ", a_list)
        if len(a_list) > 1:
            mid = len(a_list) // 2
            left_half = a_list[:mid]
            right_half = a_list[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    a_list[k] = left_half[i]
                    i += 1
                else:
                    a_list[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                a_list[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                a_list[k] = right_half[j]
                j += 1
                k += 1
        print("Merging ", a_list)
        return a_list

    def quick_sort(self, a_list):
        self.quick_sort_helper(a_list, 0, len(a_list)-1)
        return a_list

    def quick_sort_helper(self, a_list, first, last):
        if first < last:
            split_point = self.partition(a_list, first, last)
            self.quick_sort_helper(a_list, first, split_point-1)
            self.quick_sort_helper(a_list, split_point+1, last)

    def partition(self, a_list, first, last):
        pivot_value = a_list[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
                left_mark += 1
            while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
                right_mark -= 1
            if right_mark < left_mark:
                done = True
            else:
                a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
        a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
        return right_mark

    def quick_sort_2(self, a_list):
        self.quick_sort_helper_2(a_list, 0, len(a_list)-1)
        return a_listgit






a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_data = Sorting()
# print(sort_data.bubble_sort(a_list))
# print(sort_data.bubble_sort_short(a_list))
# print(sort_data.selection_sort(a_list))
# print(sort_data.insertion_sort(a_list))
# print(sort_data.shell_sort(a_list))
# print(sort_data.merge_sort(a_list))
print(sort_data.quick_sort(a_list))
# temp = a_list[0]
# print(temp, a_list[0])
# a_list[0] = a_list[1]
# print(temp, a_list[0])
# a_list[1] = temp
# print(temp, a_list[1])
# bubble_sort(a_list)
# print(a_list)