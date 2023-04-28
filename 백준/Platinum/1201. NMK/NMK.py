import sys

N, M, K = map(int, sys.stdin.readline().split())

if M + K - 1 <= N and N <= M * K:
    dp = [(i + 1) for i in range(N)]
    temp = 0
    for i in range(1, M + 1):
        tempp = min(temp + K, N - M + i)
        dp[temp:tempp] = reversed(dp[temp:tempp])
        temp = tempp
    print(*dp)
else:
    print(-1)