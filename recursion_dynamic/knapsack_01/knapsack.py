
# class Item(object):

#     def __init__(self, label, value, weight):
#         self.label = label
#         self.value = value
#         self.weight = weight

#     def __repr__(self):
#         return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)

# items = [label, value, wt]
#Find the items with the MAX val


total_weight = 8
items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]


for i, row in enumerate(items):
    print(row[i])

#why is this out of range and the example below works just fine?

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

d1 = 0
for i, row in enumerate(arr):
    d1 += row[i]
    print(row[i])




# def knapsack_items(items):

#     knapsack_weight = 0

#     if knapsack_weight >= total_weight:
#         return 0
    
#     else:


    


