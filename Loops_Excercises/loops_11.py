#Exercise 11: Print all prime numbers within a range


def prime_nums(start,end):
    print("the prime numbers between",start,"and",end,"are:")
    list1=[]
    for i in range(start,end+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            list1.append(i)
    
    return list1


test=prime_nums(1,10)

for i in test:
    print(i)
