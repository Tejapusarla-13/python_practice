#Exercise 6: Add a list of Elements to a Set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# for i in sample_list:
#     sample_set.add(i)
    
sample_set.update(sample_list)
    
print(sample_set)
