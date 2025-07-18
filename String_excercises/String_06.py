#Exercise 6: Create a mixed String using the following rules

def mixed_string(a,b):
    b=b[::-1]
    new_str=""
    
    for i in range(len(a)):
        new_str+=a[i]+b[i]
    
    return new_str
    
print(mixed_string("abc","xyz"))
    
