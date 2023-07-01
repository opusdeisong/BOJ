import sys

x = [0] * 4
y = [0] * 4


def ccw(a, b, c):
    da = [y[b] - y[a], x[b] - x[a]]
    db = [y[c] - y[a], x[c] - x[a]]
    temp = da[1] * db[0] - da[0] * db[1]
    if temp < 0:
        return -1
    elif temp > 0:
        return 1
    else:
        return 0

temp = list(map(int, sys.stdin.readline().split()))
for i in range(4):
    x[i], y[i] = temp[i * 2], temp[i * 2 + 1]

result = ccw(0, 1, 2) * ccw(0, 1, 3)

if result == -1:
    print(1)
else:
    print(0)
