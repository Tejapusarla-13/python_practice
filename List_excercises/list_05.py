#Exercise 5: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
sq_lis=[]
def lis_sq(numbers):
    for i in numbers:
        sq_lis.append(i**2)
        
    return sq_lis
    
print(lis_sq(numbers))


