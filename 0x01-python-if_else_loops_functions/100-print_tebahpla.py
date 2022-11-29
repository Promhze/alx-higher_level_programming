#!/usr/bin/python3
i = 122
while (i > 96):
    if ((i % 2) == 0):
        b = i
    else:
        b = i - 32
    print("{:c}".format(b), end="")
    i = i - 1
