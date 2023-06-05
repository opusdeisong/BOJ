import sys

A, B, C = map(int, sys.stdin.readline().split())
if A <= C < B:
    print(1)
else:
    print(0)
