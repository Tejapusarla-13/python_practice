#Exercise 18: Create Higher-Order Function

def apply_operation(fun, x, y):
    return fun(x, y)
def add(x,y):
    return x+y

print(apply_operation(add,3,5))
    
