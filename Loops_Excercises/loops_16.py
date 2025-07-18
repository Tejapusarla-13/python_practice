# Exercise 16: Calculate the cube of all numbers from 1 to a given number

def cube(num):
    str=""
    for i in range(1,num+1):
        str+=f"the current number is {i} and its cube is {i**3}"+"\n"
        
    return str 
        
print(cube(3))
