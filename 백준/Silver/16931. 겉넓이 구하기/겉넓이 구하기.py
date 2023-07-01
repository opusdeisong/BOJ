import sys

N, M = map(int, sys.stdin.readline().split())

arr = [[0] * (M + 2) for _ in range(N + 2)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(1, N + 1):
    arr[i][1:M+1] = list(map(int, sys.stdin.readline().split()))

ans = 0

for r in range(1, N + 1):
    for c in range(1, M + 1):
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if arr[r][c] >= arr[nr][nc]:
                ans += arr[r][c] - arr[nr][nc]

ans += 2 * (N * M)
print(ans)
