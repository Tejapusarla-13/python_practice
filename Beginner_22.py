# Exercise 22: Capitalize the first letter of each word in a string

def first_cap(str1):

    str2lis= str1.split(" ")

    for i in str2lis:
        print(i.capitalize(), end=" ")


    return

first_cap(str1 = "pynative.com is for python lovers")
