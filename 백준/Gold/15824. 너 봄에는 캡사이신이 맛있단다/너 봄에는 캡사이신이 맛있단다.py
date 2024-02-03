import sys

MOD = 1_000_000_007

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
two = [0] * N

temp = 1
p, m = 0, 0

for i in range(N):
    two[i] = temp - 1
    temp *= 2
    temp %= MOD

arr.sort()

for i in range(N - 1, 0, -1):
    p += two[i] * arr[i]
    m += two[i] * arr[N - 1 - i]
    p %= MOD
    m %= MOD

print((p + MOD - m) % MOD)
