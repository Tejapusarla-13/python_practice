#Exercise 19: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

def Iterate_2lists(list1,list2):
    a=""
    for i,j in zip(list1,list2):
        a+=f"{i} {j} \n"
    return a
        
print(Iterate_2lists(list1,list2))
