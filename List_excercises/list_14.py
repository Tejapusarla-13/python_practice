#Exercise 14: List Comprehension for Numbers

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

def list_Comprehension(my_list):
    new_list=[]
    for i in my_list:
        if isinstance(i,int):
            new_list.append(i)
            
    return new_list
    
print(list_Comprehension(my_list))
