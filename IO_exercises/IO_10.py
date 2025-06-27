#Exercise 10: Read Line Number 4 from File

with open("sample.txt","r") as fp:
    lines= fp.readlines()
c=1
for i in lines:
    if c==4:
        print(i)
    c+=1


#print(lines[3])
