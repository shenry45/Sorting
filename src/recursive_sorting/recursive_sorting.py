import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):

    # create blank fixed-size array for sorted elements
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # appended elements added after merger to allow full iteration and have remaining numbers added to list from conditional, loop never hits these numbers but has to be highest number than possible input to prevent adding to merged arr
    arrA.append(999999999)
    arrB.append(999999999)

    i = 0
    j = 0

    # loop through holder array
    for k in range(0, len(merged_arr)):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            # increment to next arrA item
            i += 1
        else:
            merged_arr[k] = arrB[j]
            #increment to next arrB item
            j += 1

    return merged_arr

    # for numb in arrA:
    #     for numb2 in arrB:

    #         if numb < numb2:
    #             merged_arr[arr1_index] = numb
    #             arr1_index += 1
    #             main_index += 1
    #             break
    #         else:
    #             if len(arrB) == 1 or len(arrA) == main_index:
    #                 # append B number
    #                 merged_arr[main_index] = numb2
    #                 # increase A index
    #                 arr1_index += 1

    #                 merged_arr[main_index + 1] = numb
    #             else:
    #                 merged_arr[main_index] = numb2
    #                 arr2_index += 1
    #                 main_index += 1


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        lhs = merge_sort( arr[ : len(arr) // 2 ] )
        rhs = merge_sort( arr[ len(arr) // 2 : ] )
        arr = merge(lhs,rhs)

        return arr
    else:
        return arr

    # if len(arr) == 1:
    #     return arr

    # elif len(arr) == 2:
    #     if arr[0] > arr[1]:
    #         holder = arr[0]
    #         arr[0] = arr[1]
    #         arr[1] = holder
        
    #     print(arr, '2 values')
    #     return arr

    # else:
    #     lhs = arr[:math.floor(len(arr)/2)]
    #     rhs = arr[math.floor(len(arr)/2):]
    #     return merge_sort(lhs) + merge_sort(rhs)       
        
    #     return arr


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
