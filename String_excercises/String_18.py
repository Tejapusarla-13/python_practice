# Exercise 18: Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'
def replace_char(str1):
    str2 = ""
    for i in str1:
        if i.isalpha():
            str2 += i
        elif i == " ":
            str2 += i
        else:
            str2 = str2 + "#"

    return str2

print(replace_char(str1))
