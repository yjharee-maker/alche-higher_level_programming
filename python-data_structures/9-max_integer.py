#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return "None"
    maximum = -1000000000000000000
    for i in range(len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
    return maximum
