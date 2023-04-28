import sys, math

def calc(x, y, w):
    h1 = math.sqrt(x ** 2 - w ** 2)
    h2 = math.sqrt(y ** 2 - w ** 2)
    return (h1 * h2) / (h1 + h2)


x, y, c = map(float, sys.stdin.readline().split())
s, e = 0, min(x, y)
ans = 0
while (e - s) > 1e-6:
    w = (s + e) / 2
    ans = w
    if calc(x, y, w) < c:
        e = w
    else:
        s = w

print(ans)