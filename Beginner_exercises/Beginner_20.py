# Exercise 20: Print Reverse Number Pattern

def rev_pattern(num):
    
    for i in range(1,num+1):
        for j in range(num+1,i,-1):
            print(i,end=" ")
        print()
    
        
test=rev_pattern(5)
print(test)

