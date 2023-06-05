import sys

K = int(sys.stdin.readline())
for x in range(1, K + 1):
    n, s, d = map(int, sys.stdin.readline().split())
    total_value = 0
    for _ in range(n):
        di, vi = map(int, sys.stdin.readline().split())
        if di / s <= d:
            total_value += vi
    print("Data Set {}:".format(x))
    print(total_value)
    print()
