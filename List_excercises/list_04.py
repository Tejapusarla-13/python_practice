#Exercise 4: Reverse a list
list1 = [100, 200, 300, 400, 500]
rev_list1=[]
def rev_list(list1):
    for i in list1[::-1]:
        rev_list1.append(i)
        
    return rev_list1
    
print(rev_list(list1)))
