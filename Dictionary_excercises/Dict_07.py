#Exercise 7: Access Nested Dictionary

data = {'person': {'name': 'Alice', 'age': 30}}

def access_nested_dict(data):
    for i,j in data.items():
        if isinstance(j,dict):
            for e,f in j.items():
                str1=f"{j['name']}'s age is {j['age']}"
            
    return str1
    
print(access_nested_dict(data))
    
