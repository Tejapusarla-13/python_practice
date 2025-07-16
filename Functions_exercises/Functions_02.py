#Exercise 2: Create a function with variable length of arguments

def var_func(*num):
    for i in num:
        print(i)
    
    
print("Printing values")   
var_func(20,30,40)
