#Exercise 11: Print all prime numbers within a range


start=int(input("enter start number"))
end =int(input("enter end number"))

print("the prime numbers between",start,"and",end,"are:")
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
