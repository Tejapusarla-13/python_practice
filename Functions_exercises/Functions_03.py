#Exercise 3: Return multiple values from a function


def calculation(a, b):
    sum1=a+b
    sub=a-b
    return sum1, sub
    
res = calculation(40, 10)
print(res)
