#Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def list1(a,b):
    list2=[]
    for i in range(a,b+1):
        if i%2==0:
            list2.append(i)
    return list2
    
print(list1(4,30))
