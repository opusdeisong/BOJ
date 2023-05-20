import sys

A, B, C, D = map(int, sys.stdin.readline().split())
print(abs((A + D) - (B + C)))