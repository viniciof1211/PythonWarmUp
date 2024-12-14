# Implementation of simple binarySearch on top of a given array

def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:       # stop condition
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False