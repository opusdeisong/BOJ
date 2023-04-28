MOD = int(1e9)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def matrix_mult(a, b):
    sz = len(a)
    ret = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            for k in range(sz):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= MOD
    return ret

def matrix_power(a, b):
    sz = len(a)
    ret = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        ret[i][i] = 1

    while b:
        if b % 2:
            ret = matrix_mult(ret, a)
        b //= 2
        a = matrix_mult(a, a)
    return ret

a, b = map(int, input().split())
A = [[1, 1], [1, 0]]
a = matrix_power(A, a + 1)
b = matrix_power(A, b + 2)
ans = (b[0][1] - a[0][1] + MOD) % MOD
print(ans)
