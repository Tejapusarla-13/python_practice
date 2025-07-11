#Exercise 16: Check Palindrome Number

def palindrome(num):
    num1=num
    rev_num=0
    while num1>0:
        rem=num1%10
        rev_num=rev_num*10+rem 
        num1=num1//10
        
    if rev_num==num:
        print("its a palindrome")
    else:
        print("its not a palindrome")
    
    return
    
palindrome(num=2332)
