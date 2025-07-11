# Exercise 13: Print multiplication table from 1 to 10
def multiplication_table(num):
    for i in range(1,num+1):
        for j in range(1,11):
            print(i * j ,end=" ")
        print()
    return

multiplication_table(10)
