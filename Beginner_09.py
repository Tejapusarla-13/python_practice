# Exercise 9: Check Palindrome Number

def palindrome(num):
    num=str(num)
    if num[0]== num[-1]:
        return "the number is palindrome"
    else:
        return "the number is not palindrome"
    
    
test=palindrome(num=232)

print(test)
