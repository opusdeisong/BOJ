import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(2)]
dp[0][0] = arr[0]
dp[1][0] = -1e9

for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
    
print(max(max(dp[0]), max(dp[1])))