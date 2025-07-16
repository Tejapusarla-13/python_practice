#Exercise 12: Modifies global variable
global_var=10
def test_func():
    global global_var
    global_var=15
    return global_var
    
print(test_func())
