# Exercise: 19: Print Alternate Prime Numbers till 20
lis=[]
for i in range(2,20):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lis.append(i)
print(lis)

for i in range(len(lis)):
    if i%2==0:
        print(lis[i],end=" ")
