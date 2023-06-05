import sys

N, M, K = map(int, sys.stdin.readline().split())
ans = 0
for i in range(K + 1):
    ans = max(min((N - i) // 2, M - K + i), ans)

print(ans)