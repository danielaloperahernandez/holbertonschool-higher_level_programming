#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i]/my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("Division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
