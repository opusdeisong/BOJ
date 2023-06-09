import sys

dp = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    dp[0][i] = 1
for i in range(1, 31):
    for j in range(i, 31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(dp[N][N])
    
    