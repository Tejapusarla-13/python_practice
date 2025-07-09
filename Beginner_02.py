# Exercise 2: Print the Sum of a Current Number and a Previous number
def num(a):
    for i in range(0,a+1):
        pre_num=i-1
        if pre_num<0:
            pre_num=0
        sum1=pre_num+i
        print("the current number is",i,"previous number is",pre_num,"sum is",sum1)
    
    return

num(10)
