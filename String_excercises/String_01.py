#Exercise 1A: Create a string made of the first, middle and last character

def first_middle_last(str1):
    
    new_str=str1[0]+str1[int(len(str1)/2)]+str1[-1]
    return new_str

print(first_middle_last("James"))

#Exercise 1B: Create a string made of the middle three characters

def middle_3(str1):

    a=int(len(str1)/2)
    new_str=str1[a-1]+str1[a]+str1[a+1]
    return new_str
print(middle_3("JaSonAy"))

