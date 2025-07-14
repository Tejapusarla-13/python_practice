# Exercise 4: Remove first n characters from a string
def slicing(word,number):
    number=int(number)
    result=word[number::]
    return result
test=slicing("teja",2)
print(test)

