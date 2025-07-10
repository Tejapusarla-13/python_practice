# Exercise 8: Print the following pattern

def pattern(rows):
    for i in range(1,rows+1):
        print((str(i)+" ")*i,)
    return

pattern(rows=5)

