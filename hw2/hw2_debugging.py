"""This module imports the random_array() function from rand.py and uses it to
generate, then sort a random array in ascending order using the
merge sort algorithm"""
import rand


def merge_sort(arr):
    """This function calls the recombine function in order to sort the input arr"""
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(leftArr, rightArr):
    """This function compares the parameter arrays index by index, combining them into
    a single array mergeArr that holds the sorted values."""
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]

    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
