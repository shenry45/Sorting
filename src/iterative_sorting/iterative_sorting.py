import re

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # (hint, can do in 3 loc) 

        # loop through remainder of array
        for j in range(current_index + 1, len(arr)):
        # check if each next element is smaller
            if (arr[smallest_index] > arr[j]):
        # capture index and replace with smallest
                smallest_index = j

        if (current_index != smallest_index):
            index_value_holder = arr[current_index]
            arr[current_index] = arr[smallest_index]
            arr[smallest_index] = index_value_holder

    return arr


def bubble_sort( arr ):
    element_swap_in_pass = True

    while (element_swap_in_pass == True):
        swap_counter = 0

        for i in range(0, len(arr) - 1):
            if (arr[i] > arr[i + 1]):
                value_holder = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = value_holder

                swap_counter = swap_counter + 1

        if (swap_counter == 0):
            element_swap_in_pass = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    def array_has_zero_negative_numbers():
        for i in range(0, len(arr)):
            if (arr[i] < 0):
                return False

        return True


    if len(arr) > 0 and array_has_zero_negative_numbers():
        def find_highest_arr_numb():
            if (max(arr) > len(arr)):
                return max(arr)
            else:
                return len(arr)

        count_tracker = [0 for i in range(0, find_highest_arr_numb() + 1)]

        for i in range(0, len(arr)):
            current_value = arr[i]
            count_tracker[current_value] += 1

        sorted_arr = []

        for i in range(0, len(count_tracker)):
            multiples_arr = []
            
            for j in range(0, count_tracker[i]):
                multiples_arr.append(i)

            sorted_arr += multiples_arr
            
        print(sorted_arr)

        return sorted_arr
    elif array_has_zero_negative_numbers() == False:
        return 'Error, negative numbers not allowed in Count Sort'
    else:
        return []
