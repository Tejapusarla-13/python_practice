# Exercise 21: Flatten a nested list using loops

def nested_list(lis1):
    flat_list=[]
    for i in lis1:
        if isinstance(i,int):
            flat_list.append(i)
        elif isinstance(i,list):
            for j in i:
                flat_list.append(j)

    return flat_list
print(nested_list([1, [2, 3], [4, 5, 6], 7, [8, 9]]))
 
