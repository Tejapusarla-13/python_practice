# Exercise 3: Print characters present at an even index number
def str_slice(str1):
    result=""
    print("Orginal String is  PYnative")
    print("Printing only even index chars")
    for i in str1[::2]:
        result +=i+"\n"

    return result

test=str_slice("Pynative")
print(test)
