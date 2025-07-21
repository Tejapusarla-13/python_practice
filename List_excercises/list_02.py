#Exercise 2: Perform List Manipulation


my_list = [10, 20, 30, 40, 50]

def lis_manip(my_list):
    my_list[1]=200
    a=my_list.copy()
    my_list.append(600)
    b=my_list.copy()
    my_list.insert(2,300)
    c=my_list.copy()
    my_list.remove(600)
    d=my_list.copy()
    del my_list[0]
    e=my_list.copy()
    
    return f"After changing second element: {a} \nList after appending 600:{b}\nList after inserting 300 at index 2:{c}\nList after removing 600 (by value):{d}\nList after removing element at index 0:{e}"
    
    
print(lis_manip(my_list))

