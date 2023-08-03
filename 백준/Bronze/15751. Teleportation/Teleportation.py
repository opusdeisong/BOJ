import sys

a, b, x, y = map(int, sys.stdin.readline().split())

print(min(abs(a - b), min(abs(a - x) + abs(b - y), abs(a - y) + abs(b - x))))
