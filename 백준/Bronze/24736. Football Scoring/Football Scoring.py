import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())
ans = a * 6 + b * 3 + c * 2 + d + e * 2
a, b, c, d, e = map(int, sys.stdin.readline().split())
anss = a * 6 + b * 3 + c * 2 + d + e * 2
print(ans, anss)