import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    index = 0

    for el in arrA:
        merged_arr[index] = el
        index += 1

    for el in arrB:
        merged_arr[index] = el
        index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    print(arr, 'iteration')

    if len(arr) == 1:
        return arr

    elif len(arr) == 2:
        if arr[0] > arr[1]:
            holder = arr[0]
            arr[0] = arr[1]
            arr[1] = holder
        
        print(arr, '2 values')
        return arr

    else:
        lhs = arr[:math.floor(len(arr)/2)]
        rhs = arr[math.floor(len(arr)/2):]
        return merge_sort(lhs) + merge_sort(rhs)       

    return arr

print(merge_sort([5, 1, 4, 2, 9, 6, 0, 7, 3]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
