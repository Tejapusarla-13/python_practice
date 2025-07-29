#Exercise 8: Print the value of key ‘history’ from nested dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

def access_nested_dict(sampleDict):
    return sampleDict['class']['student']['marks']['history']
    
print(access_nested_dict(sampleDict))
