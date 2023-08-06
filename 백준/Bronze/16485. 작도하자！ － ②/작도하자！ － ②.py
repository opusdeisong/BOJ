import sys

c, b = map(int, sys.stdin.readline().split())
if c % b == 0:
    print(c // b)
else:
    print(f"{c / b}")