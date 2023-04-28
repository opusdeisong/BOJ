import sys

N = int(sys.stdin.readline())
room = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
dp = [-5001 for _ in range(M + 1)]
for i in range(N - 1, -1, -1):
    temp = room[i]
    for j in range(temp, M + 1):
        dp[j] = max(dp[j - temp] * 10 + i, i, dp[j])

print(dp[M])