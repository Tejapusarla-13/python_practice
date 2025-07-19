#Exercise 16: Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'
def re_char(str1):
    str2=""
    for i in str1:
        if i.isdigit():
            str2+=i
    return str2
print(re_char(str1))
