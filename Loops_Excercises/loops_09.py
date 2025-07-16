#Exercise 9: Display numbers from -10 to -1 using for loop

def rev_nums(ran):
    list1=[]
    for i in range(ran,0):
        list1.append(i)
    return list1


test=rev_nums(-10)

for i in test:
    print(i)
    
