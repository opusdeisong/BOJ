import sys

N = 10 ** 5 + 1
mod = 20150523

DP = [[0] * N for i in range(3)]
DP[0][0] = 1
for i in range(1, N):
    for r in range(3):
        for r0 in range(3):
            DP[r][i] += DP[r0][i - 1] * (3 - 2 * int(r == r0))
        DP[r][i] %= mod

def solve(X):
    X = [*map(int, str(X))]
    L = len(X)
    for l in range(L):
        if X[l] and not X[l] % 3:
            X[l] -= 1
            X[l+1:] = [8] * (L - l - 1)
    cnt = R = 0
    for l in range(L):
        x = X[l]
        for i in range(x):
            if i and not i % 3:
                continue
            for r in range(3):
                if (R + i + r) % 3:
                    cnt += DP[r][L - l - 1]
        R += x
        R %= 3
        cnt %= mod
    return cnt + int(R != 0)

A, B = map(int, sys.stdin.readline().split())
A -= 1
print((B - A - solve(B) + solve(A)) % mod)
