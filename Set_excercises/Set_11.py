#Exercise 11: Set Intersection Check

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("the two sets have no comman elements")
else:
    print(set1.intersection(set2))
    


