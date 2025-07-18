# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

def Exercise_03(s1,s2):
    mi1=int(len(s1)/2)
    mi2=int(len(s2)/2)
    new_str=s1[0]+s2[0]+s1[mi1]+s2[mi2]+s1[-1]+s2[-1]
    return new_str
print(Exercise_03("America","Japan"))

