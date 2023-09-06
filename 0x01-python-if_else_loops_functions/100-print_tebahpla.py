#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        character = chr(i)
    else:
        character = chr(i - 32)
    print("{}".format(character), end="")
