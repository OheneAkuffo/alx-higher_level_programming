#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except (ValueError, TypeError):
            print("wrong type")
            tmp = 0
        except IndexError:
            print("out of range")
            tmp = 0
        finally:
            new_list.append(tmp)
    return (new_list)
