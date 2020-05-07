#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        return list(map(lambda elm: replace if elm == search
                        else elm, my_list))
