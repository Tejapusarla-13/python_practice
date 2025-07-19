#Exercise 10: Write a program to count occurrences of all characters within a string

str1="apple"
lis1=[]
def str2lis(str1):
    for i in str1:
        lis1.append(i)
    
    return lis1

def my_dict(lis1):
    my_dict1={}
    for i in lis1:
        if i not in my_dict1:
            my_dict1[i]=0
        if i in my_dict1:
            my_dict1[i]+=1
    return my_dict1
    
a=str2lis(str1)
print(my_dict(a))
        
        
