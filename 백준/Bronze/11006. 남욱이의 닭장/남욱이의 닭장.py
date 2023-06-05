import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    U = 2 * M - N
    T = N - M
    print(U, T)
