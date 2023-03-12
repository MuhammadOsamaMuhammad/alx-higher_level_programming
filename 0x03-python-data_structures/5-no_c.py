#!/usr/bin/python3
def no_c(my_string):
    temp = []
    for i in my_string:
        if i == 'c' or i == 'C':
           continue
        temp.append(i)
    my_string = ''.join(temp)
    return str(my_string)
