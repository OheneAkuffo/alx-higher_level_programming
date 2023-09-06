#!/usr/bin/python3
for step in range(8):
    for i in range(step+1, 10):
        print("{:d}{:d}, ".format(step, i), end="")
print("{:d}{:d}".format(step+1, i))
