# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
#     • "add {people}" – you should add the number of people in the last wagon
#     • "insert {index} {people}" - you should add the number of people at the given wagon
#     • "leave {index} {people}" - you should remove the number of people from the wagon.
#     There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train
# Sort the wagons in ascending order according to the number of people in it. Output should look like
# Wagon 1: 2 People
# Wagon 2: 4 People .....
# Test input:
# 3
# add 20
# insert 0 15
# leave 0 5
# End

# Test input:
# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge_arrays(merge_sort(left), merge_sort(right))

def merge_arrays(left, right):
    sorted_array = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][1] <= right[right_idx][1]:
            sorted_array.append(left[left_idx])
            left_idx += 1
        else:
            sorted_array.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        sorted_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_array.append(right[right_idx])
        right_idx += 1

    return sorted_array

def train_wagons():
    number_of_wagons = int(input())
    train = [[x, 0] for x in range(1, number_of_wagons + 1)]

    command = input().split()

    while not command[0] == "End":
        if command[0] == "add":
            train[-1][1] += int(command[1])
        elif command[0] == "insert":
            insert_index = int(command[1])
            insert_people = int(command[2])
            train[insert_index][1] += insert_people
        elif command[0] == "leave":
            leave_index = int(command[1])
            leave_people = int(command[2])
            train[leave_index][1] -= leave_people

        command = input().split()

    train_sorted = merge_sort(train)
    for wagon, peopple in train_sorted:
        print(f"Wagon {wagon}: {peopple} People")


train_wagons()

