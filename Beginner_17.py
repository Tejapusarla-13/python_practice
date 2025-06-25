# Exercise 17: Generate Fibonacci series up to 15 terms
num1=0
num2=1
num3=0
print(num1,num2,end=" ")
for i in range(1,10):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")