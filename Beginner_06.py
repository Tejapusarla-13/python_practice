# Exercise 6: Display numbers divisible by 5

def divisilble_5(lis):
    print("Given list is",lis)
    print("Divisible by 5")
    for i in lis:
        if i%5==0:
            print(i)
    return

divisilble_5(lis=[10, 20, 33, 46, 55])

