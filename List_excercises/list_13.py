#Exercise 13: Remove all occurrences of a specific item from a list

list1 = [5, 20, 15, 20, 25, 50 , 20]

def rem_item(list1,rem):

    for i in list1:
        if i==rem:
            list1.remove(i)
            
    return list1


print(rem_item(list1,20))
