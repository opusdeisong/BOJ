import sys

N = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0, wine[0]]
if N > 1:
    dp.append(wine[0] + wine[1])

for i in range(3, N + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + wine[i - 2] + wine[i - 1], dp[i - 2] + wine[i - 1]))
dp.sort()
print(dp[-1])