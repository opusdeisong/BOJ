import sys
temp = 1000000007
N = int(sys.stdin.readline())
dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    if i % 2 == 0:
        dp[i] = (dp[i - 1] * 2 + 1) % temp
    else:
        dp[i] = (dp[i - 1] * 2 - 1) % temp
print(dp[N])