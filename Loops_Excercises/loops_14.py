# Exercise 14: Reverse a integer number

num=int(input("enter a number"))
num1=num
rev_num=0
num
while num>0:
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10
    
print(rev_num)

