import sys

N, K = map(int, sys.stdin.readline().split())
factors = []

for i in range(1, N + 1):
    if N % i == 0:
        factors.append(i)

if len(factors) < K:
    print(0)
else:
    print(factors[K-1])
