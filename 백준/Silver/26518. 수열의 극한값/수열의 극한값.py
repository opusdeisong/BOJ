import sys

b, c, a, a2 = map(int, sys.stdin.readline().split())
ans = 1
for i in range(10000):
    ans = b + c / ans

print(ans)