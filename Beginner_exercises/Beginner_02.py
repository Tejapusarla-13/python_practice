# Exercise 2: Print the Sum of a Current Number and a Previous number

def num(a):
    str1=""
    for i in range(0,a+1):
        pre_num=i-1
        if pre_num<0:
            pre_num=0
        sum1=pre_num+i
        result=f"the current number is {i} previous number is {pre_num} sum is {sum1}"
        str1+=result+"\n"
    
    return str1

test=num(10)
print(test)
