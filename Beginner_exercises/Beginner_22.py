# Exercise 22: Capitalize the first letter of each word in a string

def first_cap(str1):
    str2lis= str1.split(" ")
    str3=""

    for i in str2lis:
       str3+= i.capitalize()+" "
    return str3

test=first_cap(str1 = "pynative.com is for python lovers")

print(test)
