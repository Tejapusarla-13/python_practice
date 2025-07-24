#Exercise 2: Perform dictionary operations
# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

def dict_ops(my_dict):
    a=my_dict.copy()
    a.pop('profession')
    
    str1=""
    for i,j in my_dict.items():
        str1=str1+i+" "+str(j)+'\n'
        

    return f"original dict: {my_dict}\nmodified dict: {a}\n{str1}"
    
print(dict_ops(my_dict))
def key_check(my_dict,key):
    return key in my_dict
print(key_check(my_dict,'age'))
