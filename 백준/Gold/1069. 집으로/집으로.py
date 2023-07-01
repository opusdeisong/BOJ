import math

x, y, d, t = map(int, input().split())

dist = math.sqrt(x * x + y * y)
jump = int(dist // d)
remain = dist - jump * d

ans = min(dist, remain + jump * t)

ans = min(ans, (jump + 1) * d - dist + (jump + 1) * t)

if jump > 0:
    ans = min(ans, (jump + 1) * t)
else:
    if dist < d:
        ans = min(ans, 2.0 * t)

print("{:.9f}".format(ans))
