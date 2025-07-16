#Exercise 5: Display numbers from a list using a loop

def displaying_numbers(list1):
    list2=[]
    for i in list1:
        if i>500:
            break
        if i>150:
            continue
        if i%5==0:
            list2.append(i)
    return list2


a=displaying_numbers([12, 75, 150, 180, 145, 525, 50])
for i in a:
    print(i)
