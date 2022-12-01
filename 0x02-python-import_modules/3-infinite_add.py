#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if (num == 1):
        print(0)
    elif (num > 2):
        a = 0
        for i in range(1, num):
            b = int(sys.argv[i])
            a = a + b
        print(a)
