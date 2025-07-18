#Exercise 5: Count all letters, digits, and special symbols from a given string

def my_count(str1):
    c=0
    d=0
    s=0
    for i in str1:
        if i.isalpha():
            c+=1 
        elif i.isdigit():
            d+=1 
    s=len(str1)-(c+d)
    return c,d,s 
    
    
        
c,d,s=my_count("pii12%$")
print(f"chars = {c}\ndigits = {d}\nsymbols = {s}")

