import sys
from collections import deque
from itertools import  combinations
import copy

def check(x, y):
    flag = True
    if 0 > x or x >= N:
        flag = False
    if 0 > y or y >= M:
        flag = False
    return flag

def BFS():
    global ans
    q = deque([])
    for i, j in virus:
        q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if check(xx, yy):
                if temp[xx][yy] == 0:
                    temp[xx][yy] = 2
                    q.append((xx, yy))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)

N, M = map(int, sys.stdin.readline().split())
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

safe = []
virus = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
for comb in combinations(safe, 3):
    temp = copy.deepcopy(arr)
    for i, j in comb:
        temp[i][j] = 1
    BFS()
print(ans)