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



# def bubble_sort( arr ):

#     return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr