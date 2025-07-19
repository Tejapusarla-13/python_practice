# Exercise 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


def rem_emptystr(str_list):
    new_list = []
    for i in str_list:
        if i == "":
            continue
        if i == None:
            continue
        else:
            new_list.append(i)
    return new_list


print(rem_emptystr(str_list))