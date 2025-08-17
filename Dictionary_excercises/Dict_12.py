#Exercise 12: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
def keys_remove(sample_dict):
    keys = ["name", "salary"]
    for i in keys:
        sample_dict.pop(i)
        
    return sample_dict
    
print(keys_remove(sample_dict))
    

