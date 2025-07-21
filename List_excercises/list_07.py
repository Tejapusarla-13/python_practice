#Exercise 7: Count Occurrences

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']

# def occur_predefined(sports):
#     return sports.count("Football")
    
    
# print(occur_predefined(sports))


#####################################
#without pre defined funtion

def occur(sports):
    c=0
    for i in sports:
        if i=="Football":
            c+=1 
        
    return c
    
print(occur(sports))
