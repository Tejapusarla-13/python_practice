#Exercise 23: Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]
c=0
for i in range(len(list1)):
    if list1[i] ==20:
        list1[i]=200
print(list1)
