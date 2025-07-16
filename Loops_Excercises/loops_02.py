#Exercise 2: Print the following pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
def pattern(rows):
    col=""
    str1=""
    for i in range(1,rows+1,1):
        col+=str(i)+" "
        str1=str1+col+"\n"
    return str1
    
print(pattern(rows=5))
    

