# Exercise 13: Split a string on hyphens

str1 = "Emma-is-a-data-scientist"


def str_split(str1):
    print("Displaying each substring")
    lis1 = str1.split("-")
    str2 = ""
    for i in lis1:
        str2 = str2 + i + "\n"
    return str2


print(str_split(str1))