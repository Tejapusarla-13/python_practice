#Exercise 15: Access Nested Lists

Nested_list=[[10, 20, 30], [44, 55, 66], [77, 87, 99]]

def Access_nested_list(Nested_list):
    for i in Nested_list:
        for j in i:
            if j == 55:
                return j 



print(Access_nested_list(Nested_list))
