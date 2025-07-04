#Exercise 6: Count the total number of digits in a number

num=2345623
lis=[]
while num>0:
    rem=num%10
    num=num//10
    lis.append(rem)
    
print("total number of digits is",len(lis))


