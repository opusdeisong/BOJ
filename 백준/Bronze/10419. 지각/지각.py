import sys

T = int(sys.stdin.readline())
for _ in range(T):
    d = int(sys.stdin.readline())
    ans = 0
    for i in range(101):
        if i + i ** 2 > d:
            break
        else:
            ans = i
    print(ans)