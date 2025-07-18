str1 = "Welcome to USA. usa awesome usa, isn't it?"
def str2lis(str1):
    str2=""
    lis1=[]
    str1=str1.replace(".","").replace(",","").replace("?","")
    str1=str1.lower()
    for i in str1:
        if i !=" ":
            str2+=i
        if i==" ":
            lis1.append(str2)
            str2=""
    lis1.append(str2)
    
    return lis1
    
def count_dict(lis1):
    
    my_dict={}
    for i in lis1:
        if i not in my_dict:
            my_dict[i]=0
        if i in my_dict:
            my_dict[i]+=1
            
    return my_dict
        
def word_occurence():
    a=str2lis(str1)
    b=count_dict(a)
    
    return f"the word usa apeared {b['usa']} times"
    
    
print(word_occurence())
