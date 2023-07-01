import math
import sys


def square(x, y, X, Y, W, H):
    return X <= x <= X + W and Y <= y <= Y + H


def dist(a1, b1, a2, b2):
    return math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


def circle(x, y, X, Y, W, H):
    return (dist(X, Y + H / 2, x, y) <= H / 2) or (dist(X + W, Y + H / 2, x, y) <= H / 2)


W, H, X, Y, P = map(float, sys.stdin.readline().split())

ans = 0

for _ in range(int(P)):
    x, y = map(float, sys.stdin.readline().split())
    if square(x, y, X, Y, W, H) or circle(x, y, X, Y, W, H):
        ans += 1

print(ans)
