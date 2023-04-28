import sys

N, K = map(int, sys.stdin.readline().split())
bag = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
bag.insert(0, [0, 0])
ans = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            ans[i][j] = ans[i - 1][j]
        else:
            ans[i][j] = max(ans[i - 1][j], ans[i - 1][j - w] + v)

print(ans[N][K])