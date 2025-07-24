#Exercise 12: Remove Duplicates from list
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

def dupli_remove(list_with_duplicates):
    list_without_duplicates=[]
    for i in list_with_duplicates:
        if i not in list_without_duplicates:
            list_without_duplicates.append(i)
            
    return list_without_duplicates
    

print(dupli_remove(list_with_duplicates))
