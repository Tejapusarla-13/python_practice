#Exercise 4: Arrange string characters such that lowercase letters should come first
def lower_upper(str1):

    lower=""
    upper=""
    for i in str1:
        if i.islower():
            lower+=i
        if i.isupper():
            upper+=i
    return lower+upper
    
print(lower_upper("PyNaTive"))
