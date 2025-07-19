# Exercise 15: Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"


def re_spec_char(str1):
    str2 = ""
    for i in str1:
        if i.isalpha():
            str2 += i
        elif i == " ":
            str2 += i
    return str2


print(re_spec_char(str1))
