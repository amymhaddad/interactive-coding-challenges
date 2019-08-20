

total_weight = 8
# items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

added_weight = []
items = [2, 2, 4, 5]

# items_to_extract = []

for i, item in enumerate(items):
    for j, item in enumerate(items):
        if items[i] + items[j] <= total_weight:
            indexes = (i, j)
            added_weight.append(indexes)
    max_wt = max(added_weight)
#     if items[i] + items[j] == max_wt:
#         items_to_extract.append(items[i])
#         items_to_extract.append(items[j])


print(max_wt)



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