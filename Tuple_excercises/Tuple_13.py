#Exercise 13: Removing Duplicates from Tuple

my_tuple = (1, 2, 2, 3, 4, 4, 5)

unique_tuples=()
for i in my_tuple:
    if i not in unique_tuples:
        unique_tuples=unique_tuples+(i,)
        
print(f"Original tuple with duplicates: {my_tuple}\nTuple with unique elements: {unique_tuples}")

