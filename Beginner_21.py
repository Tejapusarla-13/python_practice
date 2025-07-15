# Exercise 21: Check if a user-entered string contains any digits using a for loop

def num_in_str(str1):

    for i in str1:
        if i.isdigit():
            return "this string contain numbers"
            #break
    else:
        return "this is does not contain any numbers"


test=num_in_str("Pynative123Python")

print(test)
