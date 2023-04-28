import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [num[0]]
for i in range(N - 1):
    dp.append(max(dp[i] + num[i + 1], num[i + 1]))
print(max(dp))
