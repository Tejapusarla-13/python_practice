# Exercise 11: Get each digit from a number in the reverse order.

def rev_num(num):
    num1=num
    rev_num=0
    str1=""
    while num1>0:
        rem=num1%10
        rev_num1=rev_num*10+rem
        num1=num1//10
        str1+=str(rev_num)
    return str1
    
    
test=rev_num(1234)
print(test)
