# Exercise 1: Calculate the multiplication and sum of two numbers

def my_sum(a,b):
    product=a*b
    if product<1000:
        return f"the result is {product}"
    else:
        return f"the result is {a+b}"

result=my_sum(2,3)
print(result)

