# Exercise: 19: Print Alternate Prime Numbers till 20

def alt_prime(num):

    lis=[]
    str1=""
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lis.append(i)

    for i in range(len(lis)):
        if i%2==0:
            str1+=str(lis[i])+" "
    
    return str1
    

test=alt_prime(20)
print(test)
