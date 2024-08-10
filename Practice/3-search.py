# list basic
# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n
# lines, you will be given some strings. You should add them to a list and print them. After that, you should filter
# out only the strings that include the given word and print that list too.
def sort_words(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].lower()
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if len(left) == len(arr) or len(right) == len(arr):
        return arr
    return sort_words(left) + middle + sort_words(right)


def serch_strings(arr, target):
    target = target.lower()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid].lower()
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


num = int(input())
word = input()
all_strings = [input() for _ in range(num)]
strings_as_list = [s.split() for s in all_strings]
filtered_strings = []
for i in range(len(strings_as_list)):
    sorted_words = sort_words(strings_as_list[i])
    if serch_strings(sorted_words, word):
        filtered_strings.append(all_strings[i])

print(all_strings)
print(filtered_strings)

# Input 1:
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni

# Input 2:
# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes
