#Exercise 13: Find the factorial of a given number

def factorial(num1):
    num=1
    for i in range(num1,1,-1):
        num=num*i
    return num

print(factorial(5))
