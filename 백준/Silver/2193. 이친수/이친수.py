import sys

N = int(sys.stdin.readline())
dp = [1, 1, 2, 3, 5]
if N > 5:
    for i in range(5, N):
        dp.append(dp[i - 1] + dp[i - 2])
print(dp[N - 1])