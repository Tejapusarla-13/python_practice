#Exercise 17: Invert Dictionary
# Original dictionary 1: {'a': 1, 'b': 2, 'c': 3}
# Inverted dictionary 1: {1: 'a', 2: 'b', 3: 'c'}

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

def invert_dict(original_dict1):
    inverted_dict={}
    
    for i,j in original_dict1.items():
        inverted_dict[j]=i 
        
    return f"original dict: {original_dict1}\ninverted dict: {inverted_dict}"
    
print(invert_dict(original_dict1))
