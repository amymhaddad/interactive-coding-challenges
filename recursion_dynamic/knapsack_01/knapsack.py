

total_weight = 8
# items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

# added_weight = []
# items = [2, 2, 4, 5]

# items_to_extract = []

# for i, item in enumerate(items):
#     for j, item in enumerate(items):
#         if items[i] + items[j] <= total_weight:
#             added_weight.append(items[i] + items[j])
#     max_wt = max(added_weight)
#     if items[i] + items[j] == max_wt:
#         items_to_extract.append(items[i])
#         items_to_extract.append(items[j])

item_names = ['a', 'b', 'c', 'd']
values = [2, 4, 6, 9]
weights = [2, 2, 4, 5]

# for item, val, wt in list(zip(item_name, value, weight)):
#     print(item)

totals = list(zip(item_names, values, weights))

knapsack_wt = []
for i, weight in enumerate(weights):
    for j, wt in enumerate(weights):
        