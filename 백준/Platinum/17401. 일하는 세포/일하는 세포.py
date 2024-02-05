import sys

MOD = 10**9 + 7

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

T, N, D = map(int, input().split())
M = [[[0] * N for _ in range(N)] for _ in range(T + 1)]
for i in range(N):
    M[0][i][i] = 1

for i in range(1, T + 1):
    for _ in range(int(sys.stdin.readline())):
        a, b, c = map(int, input().split())
        M[i][a - 1][b - 1] = c

for i in range(1, T + 1):
    M[i] = matrix_multiply(M[i - 1], M[i])

ans = matrix_pow(M[T], D // T)
ans = matrix_multiply(ans, M[D % T])

for row in ans:
    print(' '.join(map(str, row)))