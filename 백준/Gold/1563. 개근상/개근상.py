import sys

N = int(sys.stdin.readline())
MOD = 1_000_000

dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]

dp[1][0][0] = dp[1][0][1] = dp[1][1][0] = 1

for i in range(2, N + 1):
    dp[i][0][0] = sum(dp[i - 1][0]) % MOD
    dp[i][1][0] = (sum(dp[i - 1][0]) + sum(dp[i - 1][1])) % MOD
    dp[i][0][1] = dp[i - 1][0][0] % MOD
    dp[i][1][1] = dp[i - 1][1][0] % MOD
    dp[i][0][2] = dp[i - 1][0][1] % MOD
    dp[i][1][2] = dp[i - 1][1][1] % MOD

print((sum(dp[N][0]) + sum(dp[N][1])) % MOD)
