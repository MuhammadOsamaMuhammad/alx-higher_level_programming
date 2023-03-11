#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(mylist) or idx < 0:
        return None
    return my_list[idx - 1]
