#Exercise 14: Print a downward half-pyramid pattern of stars
def star_pattern(rows):
    str1=""
    
    for i in range(rows,0,-1):
        str1+=("*"+" ")*i+"\n"
        
    return str1
    
test=star_pattern(5)
print(test)
