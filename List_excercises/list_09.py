numbers=[10, 20, 30]

def duplicate_lis(numbers):
    
    a=numbers.copy()
    a.append(40)
    
    return f"original list : {numbers}\ncopied list: {a}"
    
print(duplicate_lis(numbers))
