#Exercise 23: Create a simple countdown timer using a while loop.
def countdown(time):

    while time>0:
        print("time remaining is",time,"seconds")
        time-=1

    print("times up!!")

    return

countdown(5)
