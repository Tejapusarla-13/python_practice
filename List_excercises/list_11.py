#Exercise 11: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2=[]
def cleaning_list(list1):
    
    for i in list1:
        if i!="":
            list2.append(i)
            
    return list2
    
print(cleaning_list(list1))
