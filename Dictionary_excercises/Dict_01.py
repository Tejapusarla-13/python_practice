#Exercise 1: Perform basic dictionary operations

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
def basic_dict(my_dict):
    a=my_dict.copy()
    a['profession']='Doctor'
    b=my_dict.copy()
    b['age']=40
    return f"Original dictionary: {my_dict}\nUpdated dictionary after adding 'profession': {a}\nUpdated dictionary after modification: {b}\n{my_dict['city']}"


print(basic_dict(my_dict))
