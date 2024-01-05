#!/usr/bin/python3
"""
     A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): List of integers to find a peak in.
    Returns:
        int or None: Peak element or None if no peak is found.
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    low, high = 0, size - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
