# Exercise 15: Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def odd_indicies():
    for i in range(len(my_list)):
        if i%2!=0:
             return my_list[i]

print(odd_indicies())
