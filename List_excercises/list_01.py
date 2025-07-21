#Exercise 1: Perform Basic List Operations

my_list = [10, 20, 30, 40, 50]

def basic_lis(my_list):
    a=my_list[2]
    b=len(my_list)
    if my_list ==[]:
        c ="its an empty lis"
    else:
        c="its not a empty list"
    return f"Third item: {a} \nLength of the list: {b} \n{c}"
    
print(basic_lis(my_list))
