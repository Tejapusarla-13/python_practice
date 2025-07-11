# Exercise 11: Get each digit from a number in the reverse order.

def rev_num(num):
    num1=num
    rev_num=0
    while num1>0:
        rem=num1%10
        rev_num1=rev_num*10+rem
        num1=num1//10
    
    print(rev_num1)
    return
    
rev_num(1234)
