

total_weight = 8
# items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

added_weight = []
weights = [2, 2, 4, 5]
values = [2, 4, 6, 9]
item_names = ['a', 'b', 'c', 'd']

totals = list(zip(item_names, values, weights))

for i, item in enumerate(weights):
    for j, item in enumerate(weights):
        if weights[i] + weights[j] <= total_weight:
            indexes = (i, j)
            added_weight.append(indexes)
    max_wt = max(added_weight)
#     if items[i] + items[j] == max_wt:
#         items_to_extract.append(items[i])
#         items_to_extract.append(items[j])

max_value = 0
for value in max_wt:
    max_value += values[value]
print(max_value)
    






# item_names = ['a', 'b', 'c', 'd']
# values = [2, 4, 6, 9]
# weights = [2, 2, 4, 5]

# for item, val, wt in list(zip(item_name, value, weight)):
#     print(item)

# totals = list(zip(item_names, values, weights))

# knapsack_indexes = []
# for i, weight in enumerate(weights):
#     for j, weight in enumerate(weights):
    
#         if weights[i] + weights[j] <= total_weight:
#             indexes = (i, j)
#     knapsack_indexes.append(indexes)
#             # print(weights[i], weights[j])

# # print(max(knapsack_wt))
# print(knapsack_indexes)

# x = sorted(knapsack_indexes, key=lambda x: x[0], reverse=True)
# print(x)