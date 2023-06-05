import sys

n = int(sys.stdin.readline())

for _ in range(n):
    c, p = map(int, sys.stdin.readline().split())
    if c == 1:
        total = p
    else:
        total = p + (c-1)*(p-2)
    print(c, p)
    print(total)
