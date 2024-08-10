# finds all the zeros, and moves them to the back without messing
# up the other elements. Print the resulting integer list.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #  Промяна на сортиращото условие от arr[j] > arr[j + 1], в условие че всяко число различно
            #  от 0 минава напред
            if arr[j] == 0 and arr[j+1] != 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def move_zeros_to_end(arr):
    return bubble_sort(arr)


arr1 = [1, 0, 1, 2, 0, 1, 3]
arr2 = [0, 5, 0, 4, 0, 0, 5]

print(move_zeros_to_end(arr1))  # [1, 1, 2, 1, 3, 0, 0]
print(move_zeros_to_end(arr2))  # [5, 4, 5, 0, 0, 0, 0]
