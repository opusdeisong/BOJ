import sys

A, B, C = map(int, sys.stdin.readline().split())
if A + B + C > 4:
    print(2)
else:
    print(1)