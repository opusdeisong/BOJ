import sys
mod = 1000000

X = sys.stdin.readline().strip()
dp = [0 for _ in range(len(X) + 1)]

if X[0] != '0':
    X = "0" + X
    dp[0] = dp[1] = 1
    for i in range(2, len(X)):
        if X[i] > '0':
            dp[i] += dp[i - 1]
        if X[i - 1] != '0' and X[i - 1] + X[i] < '27':
            dp[i] += dp[i - 2]
    print(dp[len(X) - 1] % mod)
else:
    print(0)