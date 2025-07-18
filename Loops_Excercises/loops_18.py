# Exercise 18: Print the following pattern

def triangle_pattern(rows):
    str1=""
    for i in range(1,int(rows/2)):
        str1+=("* "*i)+"\n"
    for i in range(int(rows/2),0,-1):
        str1+=("* "*i)+"\n"

    return str1
    
test=triangle_pattern(10)
print(test)
