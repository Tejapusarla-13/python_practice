#Exercise 7: String characters balance Test

s1 = "Yn"
s2 = "PYnative"
def balanced_string():
    res= True
    for i in s1:
        if i in s2:
            continue
        else:
            res=False
    return res
    
print(balanced_string())

