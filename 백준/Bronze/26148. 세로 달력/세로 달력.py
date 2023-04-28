import sys

T = int(sys.stdin.readline())
date = int(sys.stdin.readline())

if ((T % 4 == 0 and T % 100 != 0) or T % 400 == 0):
    print(30)
else:
    print(29)