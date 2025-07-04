# Exercise 21: Flatten a nested list using loops

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flat_list=[]
for i in nested_list:
    if isinstance(i,int):
        flat_list.append(i)
    elif isinstance(i,list):
        for j in i:
            flat_list.append(j)
        
print(flat_list)
    
