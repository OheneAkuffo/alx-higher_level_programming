#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = list(str)
    if len(str) > n and n >= 0:
        del tmp[n]
    new_str = "".join(tmp)
    return new_str
