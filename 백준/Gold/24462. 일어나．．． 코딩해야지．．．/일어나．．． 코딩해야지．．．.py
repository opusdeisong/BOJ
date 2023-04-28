import math


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


n, d = map(int, input().split())
v = []
for i in range(n):
    t, k = map(int, input().split())
    v.append((t, k))

cnt = 0
ans = (0, 0)
for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue

        g = gcd(max(v[i][1], v[j][1]), min(v[i][1], v[j][1]))
        divisor = g * (v[i][1] // g) * (v[j][1] // g)

        a = (d - v[i][0]) // v[i][1] + 1
        b = (d - v[j][0]) // v[j][1] + 1

        if max(v[i][0], v[j][0]) % divisor == 0:
            c = max(v[i][0], v[j][0])
        else:
            c = (max(v[i][0], v[j][0]) // divisor + 1) * divisor

        if c <= d:
            c = (d - c) // divisor + 1
        else:
            c = 0

        tmp = a + b - c

        if tmp > cnt:
            cnt = tmp
            ans = (i + 1, j + 1)

print(ans[0], ans[1])
print(cnt)
