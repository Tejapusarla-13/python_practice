#Exercise 2: Append new string in the middle of a given string
def append2middle(s1,s2):
    new_str=s1[0:int(len(s1)/2)]+s2+s1[int(len(s1)/2)::]
    return new_str
    
    
print(append2middle("Ault","Kelly"))

