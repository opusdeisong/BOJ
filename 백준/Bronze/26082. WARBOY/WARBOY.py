import sys

a, b, c = map(int, sys.stdin.readline().split())
ans = (b / a) * c
print(int(ans * 3))