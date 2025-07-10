# Exercise 7: Find the number of occurrences of a substring in a string

def no_of_ocurrences(str_x):
     

    str1=""
    wrd=[]
    for i in str_x:
        if i !=" ":
            str1+=i
        if i == " ":
            wrd.append(str1)
            str1=""
    wrd.append(str1)
    print(wrd)
    my_dict={}
    for i in wrd:
        if i not in my_dict:
            my_dict[i]=0
        if i in my_dict:
            my_dict[i]+=1
    print(my_dict)

    print("Emma appeared",my_dict["Emma"],"times")
    
    return
    
no_of_ocurrences(str_x="Emma is good developer. Emma is a writer")
