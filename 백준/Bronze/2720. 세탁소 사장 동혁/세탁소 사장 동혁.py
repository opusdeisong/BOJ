import sys

T = int(sys.stdin.readline())
for _ in range(T):
    C = int(sys.stdin.readline())
    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    C %= 5
    P = C
    print(Q, D, N, P)
