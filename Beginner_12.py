
#Exercise 12: Calculate income tax

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
income = input("enter the income")
income=int(income)

if income <= 10000:
    tax = 0

elif income <= 20000:
    x = income - 10000
    tax = x * 10 / 1000

else:
    tax = 0
    tax = 10000 * 10 / 100
    tax = tax + (income - 20000) * 20 / 100

print("Tax payable is: ",tax)


