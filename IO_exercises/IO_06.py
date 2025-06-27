#Exercise 6: Write all content of a file into a new file by skipping line number 5


with open("sample.txt","r") as file1:
    lines=file1.readlines()

c=1
with open("new_sample.txt","w") as fp:
    for i in lines:
        if c==5:
            c+=1
            continue
        else:
            fp.write(i)
            c+=1
