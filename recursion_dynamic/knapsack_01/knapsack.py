

total_weight = 8

weights = [2, 2, 4, 5]
values = [2, 4, 6, 9]

#Solution 1: use enumerate 
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


#Solution 2: use range()
def max_weight(weights):
    added_weight = []
    for outer in range(len(weights)):
        for inner in range(len(weights)):
            if weights[outer] + weights[inner] <= total_weight:
                indexes = (outer, inner)
                added_weight.append(indexes)
    return max(added_weight)

def total_value(values):
    total_value = 0
    for index in max_weight(weights):
        total_value += values[index]
    return total_value


# def recur_wt(weights):
#     if weights == []:
#         return 0
    
#     else:
#         index = 0
#         added_weight = []
#         if weights[index] + weights[index+1] <= total_weight:
#             indexes = (index, index+1)
#             added_weight.append(indexes)
    
#     return added_weight + recur_wt(weights)

# print(recur_wt(weights))