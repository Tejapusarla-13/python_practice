#Exercise 4: Print multiplication table of a given number

def multiplication_table(num):
    str1=""
    for i in range(1,11,1):
        str1+=str(num*i)+" "
    return str1
    
print(multiplication_table(2))

