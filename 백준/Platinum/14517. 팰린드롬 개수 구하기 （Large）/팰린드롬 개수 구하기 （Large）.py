MOD = 10007

S = input()
n = len(S)
dp = [[0 for _ in range(n)] for _ in range(n)]

for length in range(1, n + 1):
    for s in range(n - length + 1):
        e = s + length - 1

        if s == e:
            dp[s][e] = 1
        else:
            dp[s][e] = (dp[s][e - 1] + dp[s + 1][e]) % MOD
            dp[s][e] -= dp[s + 1][e - 1]
            if dp[s][e] < 0:
                dp[s][e] += MOD

            if S[s] == S[e]:
                dp[s][e] = (dp[s][e] + dp[s + 1][e - 1] + 1) % MOD

print(dp[0][n - 1] % MOD)