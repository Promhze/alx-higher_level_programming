#!/usr/bin/python3
for i in range(9):
    for b in range(i + 1, 10):
        if (i == 8):
            print("{}{}".format(i, b))
        else:
            print("{}{}".format(i, b), end=", ")
