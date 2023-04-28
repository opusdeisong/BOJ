import sys

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(sys.stdin.readline())
S = [int(sys.stdin.readline()) for _ in range(N)]
K = int(sys.stdin.readline())

r = [[(j * 10 ** len(str(S[i])) + S[i]) % K for j in range(K)] for i in range(N)]
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for b in range(1 << N):
    for i in range(N):
        if b & (1 << i): continue
        for j in range(K):
            dp[b|(1 << i)][r[i][j]] += dp[b][j]
p = dp[(1 << N) - 1][0]
q = sum(dp[(1 << N) - 1])
g = GCD(p, q)

print(f"{p // g}/{q // g}")