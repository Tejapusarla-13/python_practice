# Exercise 14: Reverse a integer number

def my_rev_num(num):

    num1=num
    rev_num=0
    str1=""
    a=""
    while num>0:
        rem=num%10
        rev_num=rev_num*10+rem
        num=num//10
        
    return rev_num


print(my_rev_num(123))


