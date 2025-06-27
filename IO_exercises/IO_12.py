# Exercise 12: Interactive Menu

# 1. Say Hello 
# 2. Calculate Square
# 3. Exit

while True:
    num=int(input("enter a number"))
    if num ==1:
        print("Say hello")
    elif num==2:
        sq=int(input("enter a number"))
        print(sq**2)
    elif num==3:
        print("exit")
        break
