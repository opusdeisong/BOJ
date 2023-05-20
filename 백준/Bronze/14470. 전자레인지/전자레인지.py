import sys

info = [int(sys.stdin.readline()) for _ in range(5)]

ans = 0

if info[0] < 0:
    ans += abs(info[0]) * info[2] + info[3]
    info[0] = 0
ans += info[4] * (info[1] - info[0])

print(ans)