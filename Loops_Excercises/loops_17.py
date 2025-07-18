# Exercise 17: Find the sum of a series of a number up to n terms
# 2+22+222+2222+22222=2469


def pattern_addtion(rows):
    num=0
    for i in range(1,rows+1):
        num=int("2"*i)+num
    return num
print(pattern_addtion(5))
    
    
