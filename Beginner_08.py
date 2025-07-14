# Exercise 8: Print the following pattern

def pattern(rows):
    str1=""
    for i in range(1,rows+1):
        str1+=(str(i)+" ")*i+"\n"
    return str1

test=pattern(rows=5)
print(test)
