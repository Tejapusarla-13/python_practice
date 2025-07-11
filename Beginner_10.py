#Exercise 10: Merge two lists using the following condition

def merged_list(lis1,lis2):
    merg_lis=[]
    for i in lis1:
        if i%2!=0:
            merg_lis.append(i)
    for i in lis2:
        if i%2==0:
            merg_lis.append(i)
    print("result list:",merg_lis)
    return
    
merged_list(lis1=[10, 20, 25, 30, 35],lis2=[40, 45, 60, 75, 90])
