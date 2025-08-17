#Exercise 13: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}


def check_value(sample_dict,value):
    for i in sample_dict.values():
        if i == value:
            return f"{value} is present is the dictionary"
    else:
        return f"{value} is not present is the dictionary"
        
print(check_value(sample_dict,200))
