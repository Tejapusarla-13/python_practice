#Exercise 11: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

#Keys to extract

def keys_extract(sample_dict):
    new_dict={}
    keys = ["name", "salary"]
    for i in keys:
        new_dict[i]=sample_dict[i]
        
    return new_dict 
print(keys_extract(sample_dict))
    

