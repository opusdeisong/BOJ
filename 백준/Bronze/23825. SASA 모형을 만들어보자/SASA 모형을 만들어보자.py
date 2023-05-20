import sys

N, M = map(int, sys.stdin.readline().split())

ans = min(N // 2, M // 2)
print(ans)