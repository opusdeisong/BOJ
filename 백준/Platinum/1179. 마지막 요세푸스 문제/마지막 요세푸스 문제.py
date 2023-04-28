import sys

class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)


def calc(N, K):
    if N == 1:
        return 0
    if K == 1:
        return N - 1
    if (K <= N):
        temp = N - N // K
        tempp = calc(temp, K) - N % K
        if tempp < 0:
            tempp += temp
        return (K * (tempp % temp)) // (K - 1)
    else:
        return (calc(N - 1, K) + K) % N

N, K = map(int, sys.stdin.readline().split())
with recursion_depth(20000):
    ans = calc(N, K) + 1
print(ans)