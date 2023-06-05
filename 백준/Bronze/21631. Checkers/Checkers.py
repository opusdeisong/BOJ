import sys

a, b = map(int, sys.stdin.readline().split())

if a >= b:
    print(b)
else:
    print(a + 1)