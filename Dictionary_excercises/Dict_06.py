#Exercise 6: Count Character Frequencies

string1 = 'Jessa'
dict1={}
def count_occuer(string1):
    for i in string1:
        if i not in dict1:
            dict1[i]=0
        if i in dict1:
            dict1[i]+=1 
            
    return f"Frequencies for {string1}: {dict1}"
    
    
print(count_occuer(string1))
