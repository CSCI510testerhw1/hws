"""This module imports the random_array() function from rand.py and uses it to
generate, then sort a random array in ascending order using the
merge sort algorithm"""
import rand
import pdb

def merge_sort(arr):
    """This function calls the recombine function in order to sort the input arr"""
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """This function compares the parameter arrays index by index, combining them into
    a single array mergeArr that holds the sorted values."""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    #breakpoint()
    while left_index < len(left_arr) and right_index < len(right_arr):
        #print(left_arr)
        #print(right_arr)
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1 #increment after placing in merge_arr
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1 #increment after placing in merge_arr

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    #print(merge_arr)
    return merge_arr


test_arr = rand.random_array([None] * 20)
arr_out = merge_sort(test_arr)

print(arr_out)
