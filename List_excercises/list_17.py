#Exercise 17: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def Concatenate_indexwise(list1,list2):
    list3=[]
    for i in range(len(list1)):
        a=list1[i]+list2[i]
        list3.append(a)
        
    return list3


print(Concatenate_indexwise(list1,list2))
        

