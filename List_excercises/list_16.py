#Exercise 16: Flatten Nested List

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]

def flatten_list(list_of_lists):
    flatten_list=[]
    
    for i in list_of_lists:
        for j in i:
            flatten_list.append(j)
            
    return flatten_list


print(flatten_list(list_of_lists))
