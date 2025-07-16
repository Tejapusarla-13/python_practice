#Exercise 16: Check Palindrome Number

def palindrome(num):
    num1=num
    rev_num_value=0
    
    def rev_num(num1):
        nonlocal rev_num_value
        while num1>0:
            rem=num1%10
            rev_num_value=rev_num_value*10+rem 
            num1=num1//10
        
    rev_num(num1)
    if rev_num_value==num:
        return "its a palindrome"
    else:
        return "its not a palindrome"
    
    
test=palindrome(num=2382)
print(test)
