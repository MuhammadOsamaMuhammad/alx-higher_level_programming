#!/usr/bin/python3
def no_c(my_string):
    temp = ''
    for i in my_string:
        if i in 'cC':
           continue
        temp += i
    return temp
