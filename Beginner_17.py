# Exercise 17: Generate Fibonacci series up to 15 terms

def fibonacci(num):
    print("Fibonacci sequence:")
    num1=0
    num2=1
    num3=0
    str1=""
    print(num1,num2,end=" ")
    for i in range(1,num+1):
        num3=num1+num2
        num1=num2
        num2=num3
        str1+=str(num3)+" "
        
    return str1


test=fibonacci(num=13)
print(test)
