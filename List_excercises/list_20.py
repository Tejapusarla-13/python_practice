#Exercise 20: Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def new_item_append(list1):
    for i in list1:
        if isinstance(i,list):
         for j in i:
            if isinstance(j,list):
                for h in j:
                    if h == 6000:
                        j.append(7000)
                    
    return list1
    
print(new_item_append(list1))
        
