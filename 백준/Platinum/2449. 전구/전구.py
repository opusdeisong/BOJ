import sys

INF = 1 << 30

N, K = map(int, input().split())
a = [0] + [int(x) for x in input().split()]

a = [a[i] for i in range(len(a)) if i == 0 or a[i] != a[i - 1]]
N = len(a) - 1

dp = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 0

for size in range(2, N + 1):
    for start in range(1, N - size + 2):
        end = start + size - 1
        for mid in range(start, end):
            new_value = dp[start][mid] + dp[mid + 1][end]
            if a[start] != a[mid + 1]:
                new_value += 1
            if dp[start][end] > new_value:
                dp[start][end] = new_value

print(dp[1][N])
