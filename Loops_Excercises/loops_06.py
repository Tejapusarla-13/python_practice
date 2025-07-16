#Exercise 6: Count the total number of digits in a number

def my_count(num):
    lis=[]
    while num>0:
        rem=num%10
        num=num//10
        lis.append(rem)
    return f"total number of digits is {len(lis)}"


print(my_count(123456))


