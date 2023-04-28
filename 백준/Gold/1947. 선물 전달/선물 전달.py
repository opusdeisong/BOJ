import sys

N = int(sys.stdin.readline())
temp = 1_000_000_000


if N >= 4:
    dp = [0 for _ in range(N + 1)]
    for i in range(3):
        dp[i + 1] = i
    for i in range(4, N + 1):
        dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % temp
else:
    dp =[0]
    for i in range(N):
        dp.append(i)
print(dp[N])
