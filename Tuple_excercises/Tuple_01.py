#Exercise 1: Perform Basic Tuple Operations
my_tuple=(1,2,3,4,5,6)

def my_tup(my_tuple):
    
    a=my_tuple[2]
    b=len(my_tuple)
    
    return f"My tuple: {my_tuple}\nThe third element of my_tuple: {a}\nThe length of my_tuple: {b}"
    

print(my_tup(my_tuple))
