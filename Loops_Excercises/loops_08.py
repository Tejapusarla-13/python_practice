# Exercise 8: Print list in reverse order using a loop

def rev_order_print(list1):
    list2=[]
    for i in list1[::-1]:
        list2.append(i)
    return list2


print(rev_order_print([10, 20, 30, 40, 50]))
        
