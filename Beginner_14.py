
#Exercise 14: Print a downward half-pyramid pattern of stars
def star_pattern(rows):

    for i in range(rows,0,-1):
        print(("*"+" ")*i)
    return
star_pattern(5)
