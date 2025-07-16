#Exercise 10: Call Function using both positional and keyword arguments

def describe_pet(animal_type, pet_name):
    return animal_type,pet_name
    
print(describe_pet("teja","human"))
print(describe_pet(animal_type="teja",pet_name="human"))
