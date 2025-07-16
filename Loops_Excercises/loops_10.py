#Exercise 10: Display a message “Done” after the successful execution of the for loop

def done_msg(ran):
    list1=[]
    for i in range(1,ran+1):
        list1.append(i)
    return list1

test=done_msg(5)
for i in test:
    print(i)

print("Done")
