#Exercise 17: Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"
def alpha_digit(str1):
    str2= str1.split(" ")
    str3=""
    for i in str2:
        if i.isalpha():
            continue
        else:
           str3=str3+i+"\n"
    return str3

print(alpha_digit(str1))