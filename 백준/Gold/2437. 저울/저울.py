import sys

N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()

ans = 1

for i in weight:
    if ans < i:
        break

    ans += i
print(ans)