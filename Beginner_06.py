# Exercise 6: Display numbers divisible by 5

def divisilble_5(lis):
    str1=""
    print("Given list is",lis)
    print("Divisible by 5")
    for i in lis:
        if i%5==0:
           str1+=str(i)+"\n" 
    return str1

test=divisilble_5(lis=[10, 20, 33, 46, 55])
print(test)
