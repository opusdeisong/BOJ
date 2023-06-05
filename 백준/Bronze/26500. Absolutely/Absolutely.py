import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    distance = abs(x - y)
    print("{:.1f}".format(distance))