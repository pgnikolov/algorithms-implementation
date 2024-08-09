# list advanced
# Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending
# order (alphabetically). Print the resulting list.

def alphabetic_compare(name1, name2):
    for i in range(len(name1)):
        if ord(name1[i]) == ord(name2[i]):
            continue
        elif ord(name1[i]) != ord(name2[i]):
            return ord(name1[i]) - ord(name2[i])


def sort_names(names):
    n = len(names)
    for i in range(n):
        for j in range(n - i - 1):
            if len(names[j]) < len(names[j + 1]):
                names[j], names[j + 1] = names[j + 1], names[j]
            elif len(names[j]) == len(names[j + 1]):
                if alphabetic_compare(names[j], names[j + 1]) > 0:
                    names[j], names[j + 1] = names[j + 1], names[j]


names_1 = ['Ali', 'Marry', 'Kim', 'Teddy', 'Monika', 'John']
names_2 = ['Lilly', 'Tim', 'Kate', 'Tom', 'Alex']

sort_names(names_1)
print(names_1)
sort_names(names_2)
print(names_2)
