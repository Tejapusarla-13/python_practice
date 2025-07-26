#Exercise 3: Dictionary from Lists

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
def list_dict(keys,values):
    new_dict={}
    for i,j in zip(keys,values):
        new_dict[i]=j
    return new_dict
print(list_dict(keys,values))
