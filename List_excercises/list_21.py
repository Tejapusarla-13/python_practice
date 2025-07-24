#Exercise 22: Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2=["h", "i", "j"]
# def new_item_append(list1):
#     for i in list1:
#         if isinstance(i,list):
#          for j in i:
#             if isinstance(j,list):
#                 for h in j:
#                     if isinstance(h,list):
#                         h.extend(list2)
                    
#     return list1
    
# print(new_item_append(list1))

###################

list1[2][1][2].extend(list2)
print(list1)
        
