# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Test input 1:
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
# Test Input 2:
# 3-C
# 2-A
# 1-B
# 6-V
# End

def to_do():
    to_do_list = []
    while True:
        command = input()
        if command == "End":
            break
        actions = command.split("-")
        priority = int(actions[0])
        note = actions[1]
        to_do_list.append([priority, note])

    n = len(to_do_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if to_do_list[j][0] > to_do_list[j + 1][0]:
                to_do_list[j], to_do_list[j + 1] = to_do_list[j + 1], to_do_list[j]

    # for note in to_do_list:
    return [note[1] for note in to_do_list]

print(to_do())