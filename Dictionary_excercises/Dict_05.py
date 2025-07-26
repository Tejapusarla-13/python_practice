#Exercise 5: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
def merge_dicts(dict1,dict2):
    for i,j in dict2.items():
        if i not in dict1:
            dict1[i]=j
            
    return dict1

print(merge_dicts(dict1,dict2))

