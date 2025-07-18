#Exercise 20: Print the alternate numbers pattern
#OUTPUT:
# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15
def alt_pattern():
    c=1
    str1=""
    for i in range(1,6):
        for j in range(1,i+1):
            str1+=str(c)+" "
            c+=1
        str1+="\n"
    return str1
    
print(alt_pattern())

