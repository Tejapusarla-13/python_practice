#Exercise 9: Modify Nested Dictionary
nested_student_dict = {
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

def Modify_nested_dict(nested_student_dict):
    nested_student_dict['class']['student']['name']="Jessa"
    
    return nested_student_dict
    
print(Modify_nested_dict(nested_student_dict))
