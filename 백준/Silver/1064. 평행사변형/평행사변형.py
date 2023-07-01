import math
import sys


def length(x1, y1, x2, y2, x3, y3):
    ans = 0
    ans += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ans += math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    return ans * 2.0


def check(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)


x = []
y = []
ans = []
temp = list(map(int, sys.stdin.readline().split()))
for i in range(3):
    x.append(temp[i*2])
    y.append(temp[i * 2 + 1])

if not check(x[0], y[0], x[1], y[1], x[2], y[2]):
    print(-1)
else:
    for i in range(3):
        ans.append(length(x[i], y[i], x[(i + 1) % 3], y[(i + 1) % 3], x[(i + 2) % 3], y[(i + 2) % 3]))

    ans.sort()
    print("{:.10f}".format(ans[2] - ans[0]))
