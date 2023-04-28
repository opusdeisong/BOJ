import sys
N, M, K = map(int, sys.stdin.readline().split())
dp = [[1] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[N][M] >= K:
    ans = ""
    while 1:
        if N == 0 or M == 0:
            ans += "z" * M
            ans += "a" * N
            break
        temp = dp[N - 1][M]

        if K <= temp:
            ans += "a"
            N -= 1
        else:
            ans += "z"
            M -= 1
            K -= temp
    print(ans)
else:
    print(-1)