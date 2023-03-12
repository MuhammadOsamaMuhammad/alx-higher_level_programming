#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    n = []
    i = 0
    while i < len(my_list):
        if i == idx:
            pass
        n.append(my_list[i])
        i = i + 1
    return n
