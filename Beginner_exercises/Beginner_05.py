# Exercise 5: Check if the first and last numbers of a list are the same
def first_last_same(lis1):

    if lis1[0]==lis1[-1]:
        return True
    else:
        return False
    

test=first_last_same([10,22,32,43,10])

print(test)
