#Exercise 14: Filter Tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
lis=[]
for i in students:
    if i[1]>=90:
        lis.append(i)
        
print(lis)
