import sys

MOD = 1_000_003

def matrix_multiply(a, b):
    N = len(a)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j] % MOD
                result[i][j] %= MOD
    return result

def matrix_pow(x, k):
    N = len(x)
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while k:
        if k % 2:
            result = matrix_multiply(result, x)
        x = matrix_multiply(x, x)
        k //= 2
    return result


N, S, E, T = map(int, sys.stdin.readline().split())
A = [[0 for _ in range(5 * N + 1)] for _ in range(5 * N + 1)]
ans = [[0 if i != j else 1 for j in range(5 * N + 1)] for i in range(5 * N + 1)]

for i in range(1, N + 1):
    s = sys.stdin.readline().rstrip()
    for j in range(len(s)):
        if int(s[j]) >= 1:
            A[i * 5][(j + 1) * 5 - (int(s[j]) - 1)] = 1
    for j in range(1, 5):
        A[(i - 1) * 5 + j][(i - 1) * 5 + j + 1] = 1

ans = matrix_pow(A, T)

print(ans[5 * S][5 * E])