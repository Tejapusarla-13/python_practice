#Exercise 14: Rename key of a dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

#output:{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

def key_rename(sample_dict):
    sample_dict["location"] = sample_dict.pop("city")
    
    return sample_dict
    
print(key_rename(sample_dict))
