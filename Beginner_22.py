# Exercise 22: Capitalize the first letter of each word in a string

str1 = "pynative.com is for python lovers"
str2lis= str1.split(" ")

for i in str2lis:
    print(i.capitalize(), end=" ")