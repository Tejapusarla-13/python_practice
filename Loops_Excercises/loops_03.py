#Exercise 3: Calculate sum of all numbers from 1 to a given number


#num1=int(input("enter a number"))
def sum_of_numbers(num):
    num1=0
    for i in range(1,num+1):
        num1 = num1+i
    return num1
    
print(sum_of_numbers(10))
