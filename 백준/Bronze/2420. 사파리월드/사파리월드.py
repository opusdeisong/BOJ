import sys
N, M = map(int, sys.stdin.readline().split())

ans = N - M
if ans > 0:
    print(ans)
else:
    print(-ans)