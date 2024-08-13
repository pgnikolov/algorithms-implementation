def knapsack(items, max_weight):
    # лист със индекси всички килограми от 0 до 850 като индекси на които да се записва стойност
    bag = [0 for _ in range(max_weight + 1)]
    # празе лист от празни листи за запазване на максимална двойка за всека тежест
    item_selection = [[] for _ in range(max_weight + 1)]

    # итерираме през всички двоики
    for weight, value in items:
        # проверяваме за максимална стойност от 850 тежест до текушата
        for wght in range(max_weight, weight - 1, -1):
            # ако сегашната стойност на позиция wght в bag е по-малка от тази на елемнта намираще се на индекс разликата
            # wght - weight събран с стойноста на текушата двойка - я променяме
            if bag[wght - weight] + value > bag[wght]:
                bag[wght] = bag[wght - weight] + value
                # записваме двойката която влиза в баг
                item_selection[wght] = item_selection[wght - weight] + [(weight, value)]
                # print(item_selection)
                # print(item_selection[wght])
    # Максималната стоиност - макс индеск от баг
    max_value = bag[max_weight]
    # двоиките от макс стойност са в лист с индекс макс тегло
    selected_items = item_selection[max_weight]

    # теглото на всички избрани двойки
    total_weight = sum(item[0] for item in selected_items)

    return max_value, selected_items, total_weight


values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
          78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
          87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
          312]
weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
           42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
           3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]

weight_limit = 850

pairs = list(zip(weights, values))

# pairs = [(2, 3), (3, 4), (4, 5), (5, 6)]
#
# weight_limit = 5

bag_total_value, bag_selected_items, bag_total_weight = knapsack(pairs, weight_limit)

print("total_value:", bag_total_value)
print("selected_items:", bag_selected_items)
print("pairs_total_weight:", bag_total_weight)
