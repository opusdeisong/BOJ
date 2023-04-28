import sys

X, Y = map(int, sys.stdin.readline().split())

Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    ans = 0
    l, r = 1, X

    while l <= r:
        m = (l + r) // 2

        if (Y + m) * 100 // (X + m) > Z:
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)