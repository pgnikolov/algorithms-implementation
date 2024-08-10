# Functions-Exercise
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order.

def bubble_srot_nums(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_srot_nums([6, 2, 4, ]))
print(bubble_srot_nums([12, 52, 11, 53, 2, 8, 45, ]))


def quick_sort_nums(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_nums(left) + middle + quick_sort_nums(right)


print(quick_sort_nums([6, 2, 4, ]))
print(quick_sort_nums([12, 52, 11, 53, 2, 8, 45, ]))
