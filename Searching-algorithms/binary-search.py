# O(log n)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [1, 3, 5, 7, 9]
target = 7
result = binary_search(nums, target)
print(result)
