import sys

N, M = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
B = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(B) + 1)] for _ in range(N + 1)]
result = sum(B)

for i in range(1, N + 1):
    byte, cost = A[i], B[i]

    for j in range(1, sum(B) + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])

        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else:
    print(0)