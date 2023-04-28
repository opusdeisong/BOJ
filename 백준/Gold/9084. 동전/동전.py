import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for coin in C:
        for i in range(M + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[M])