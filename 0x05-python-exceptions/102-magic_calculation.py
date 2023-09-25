#!/usr/bin/python3
def magic_calculation(a, b):
    total_sum = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            total_sum += a ** b / i
        except Exception:
            total_sum = b + a
            break
    return total_sum
