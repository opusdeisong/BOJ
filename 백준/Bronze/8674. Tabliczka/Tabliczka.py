import sys

a, b = map(int, sys.stdin.readline().split())
if a % 2 == 1 and b % 2 == 1:
    print(min(a, b))
else:
    print(0)