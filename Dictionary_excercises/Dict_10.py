#Exercise 10: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict={}
for i in employees:
    new_dict[i]=defaults
    
print(new_dict)
