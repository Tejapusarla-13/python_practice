#Exercise 3: Sum and average of all numbers in a list
my_list = [10, 20, 30, 40, 50]

def sum_avg(my_list):
    a=0
    for i in my_list:
        a+=i
    avg=a/len(my_list)
    
    return f"the sum is: {a}\nthe average is: {avg}"
    

print(sum_avg(my_list))
