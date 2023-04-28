import sys
A = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    A.append(int(sys.stdin.readline()))

for i in range(1, M + 1):
    for j in range(len(A) - 1):
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]
for i in A:
    print(i)