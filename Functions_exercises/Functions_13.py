#Exercise 13: Write a recursive function to calculate the factorial

def factorial(num):
    if num==0:
        return 1
    return num* factorial(num-1)
    
print(factorial(5))
