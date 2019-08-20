

total_weight = 8
# items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

added_weight = []
weights = [2, 2, 4, 5]
values = [2, 4, 6, 9]

def max_weight(weights):
    """Given a total knapsack weight, get the indexes for the items that don't exceed the total weight"""
    added_weight = []
    for i, item in enumerate(weights):
        for j, item in enumerate(weights):
            if weights[i] + weights[j] <= total_weight:
                indexes = (i, j)
                added_weight.append(indexes)
    return max(added_weight)

def total_value(values):
    """Return the total item value for the maximum items the knapsack can hold based on weight"""

    item_indexes = max_weight(weights)
    max_value = 0
    for value in item_indexes:
        max_value += values[value]
    return max_value
