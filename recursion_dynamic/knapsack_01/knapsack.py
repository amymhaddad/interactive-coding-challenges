
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

weight_total = []

# for i, item in enumerate(items):
#     print(item[-1] + item[-1])
#     # print(item)
   
weights = [2, 2, 4, 5]
item_weight_used = []

# for outer in range(len(weights)):
#     for inner in range(len(weights)):
#         added_items = weights[outer] + weights[inner]
        
#         if added_items <= total_weight:
#             weight_total.append(added_items)
#             # print(weights[inner])
# #         # item_weight_used.append()
            
#     print(max(weight_total))
# # print(max(weight_total))


for i, outer in enumerate(items):
    for j in inner enumerate(items):
        print(items[-2])



item_val_wt = {
    'a': [2, 2], 
    'b': [4, 2],
    'c': [6, 4],
    'd': [9, 5],
}

# for weight in weights:
    # print(weight)
    
# def knapsack_items(items):

#     knapsack_weight = 0

#     if knapsack_weight >= total_weight:
#         return 0
    
#     else:


    


