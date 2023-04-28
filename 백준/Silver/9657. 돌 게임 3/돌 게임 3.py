import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 1

for i in range(5, N + 1):
    dp[i] = 2
    if dp[i-1] % 2 == 0 or dp[i-3] % 2 == 0 or dp[i-4] % 2 == 0:
        dp[i] = 1

if dp[N] == 1:
    print("SK")
else:
    print("CY")
