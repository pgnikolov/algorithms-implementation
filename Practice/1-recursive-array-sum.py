# Write a program that finds the sum of all elements in an integer array. Use recursion.

def sum_array(arr, indx=0):
    if indx >= len(arr) - 1:
        return arr[indx]
    return arr[indx] + sum_array(arr, indx + 1)


nums = [1, 2, 3, 4]
print(sum_array(nums))
