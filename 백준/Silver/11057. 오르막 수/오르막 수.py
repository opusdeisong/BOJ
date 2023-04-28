import sys

N = int(sys.stdin.readline())
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N):
    temp = dp.copy()
    dp = [0 for j in range(10)]
    for j in range(10):
        for k in range(j, 10):
            dp[k] += temp[j]

print(sum(dp) % 10007)
