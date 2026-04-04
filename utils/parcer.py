
def str_parcer(string):
    str_list = string.split(",")
    upper_list = []
    for i in str_list:
        upper_list.append(i.upper())
    return upper_list

