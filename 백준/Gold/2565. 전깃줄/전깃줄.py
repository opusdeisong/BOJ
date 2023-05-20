import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key = lambda x:x[0])

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))