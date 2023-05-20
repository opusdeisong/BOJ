import sys

x, N = map(int, sys.stdin.readline().split())
for _ in range(N):
    if x % 2 == 0:
        x //= 2
        x = x ^ 6
    else:
        x *= 2
        x = x ^ 6
print(x)