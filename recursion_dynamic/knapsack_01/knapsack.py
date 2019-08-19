
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
# items = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

added_weight = []
items = [2, 2, 4, 5]

items_to_extract = []

for i, item in enumerate(items):
    for j, item in enumerate(items):
        if items[i] + items[j] <= total_weight:
            added_weight.append(items[i] + items[j])
    max_wt = max(added_weight)
    if items[i] + items[j] == max_wt:
        items_to_extract.append(items[i])
        items_to_extract.append(items[j])

# print(items_to_extract)

# x = [2, 5, 2, 5]
#I get the correct item weights but I need another conditional so I get the last 2 numbers in the returned sequence based on the values they return. I want the largest value.

x = [['a', 2, 2], ['b', 4, 2], ['c', 6, 4], ['d', 9, 5]]

# def find_item(x):




    


