#!/usr/bin/python3
def uppercase(str):
    for b in str:
        b = ord(b)
        if (b >= 97) and (b <= 122):
            b = b - 32
        else:
            b = b
        print("{:c}".format(b), end="")
    print('')
