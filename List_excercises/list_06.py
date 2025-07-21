#Exercise 6: Find Maximum and Minimum

data = [8, 2, 15, 1, 9]

def max_min(data):
    data_max=data[0]
    data_min=data[0]
    for i in data[1:]:
        if i>data_max:
            data_max=i
        if i<data_min:
            data_min=i
    
    return f"the max is: {data_max}\nthe min is: {data_min}"
    
print(max_min(data))
