#Exercise 5: Create an inner function

def outer_function(a,b):
    def inner_function(a,b):
        sum1=a+b
        return sum1
    
    result=inner_function(a,b)
    
    return result+5
    
    
print(outer_function(2,3))
