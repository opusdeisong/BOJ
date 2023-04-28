import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(list(map(int, input().split())) for _ in range(N))
ans = 1e9
h = []
c = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        elif arr[i][j] == 1:
            h.append([i, j])
        elif arr[i][j] == 2:
            c.append([i, j])

for i in combinations(c, M):
    temp = 0
    for j in h:
        leng = 1e9
        for k in i:
            leng = min(leng, abs(j[0] - k[0]) + abs(j[1] - k[1]))
        temp += leng
    ans = min(ans, temp)
print(ans)