# Exercise 22: Find largest and smallest digit in a number
# Largest digit in 9876543210: 9
# Smallest digit in 9876543210: 0


num = 9876543210
s_num=str(abs(num))
largest=int(s_num[0])
smallest=int(s_num[0])

for i in s_num[1:]:
    if largest<int(i):
        largest=int(i)
    if smallest>int(i):
        smallest=int(i) 

print(f"the largest digit in {num} is {largest}")
print(f"the smallest digit in {num} is {smallest}")
