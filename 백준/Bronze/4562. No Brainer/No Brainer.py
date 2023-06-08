import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x >= y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")
