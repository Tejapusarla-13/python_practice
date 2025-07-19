def sum_avg(str1):
    c=0
    my_sum=0
    for i in str1:
        if i.isdigit():
            c+=1
            my_sum+=int(i)
    
    avg=my_sum/c
    
    return f"the sum is {my_sum} average is {avg}"
    
print(sum_avg(str1 = "PYnative29@#8496"))
            
