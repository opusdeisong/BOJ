import sys
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visit = [False] * (N + 1)
    visit[a] = True
    while q:
        temp, dist = q.popleft()

        if temp == b:
            return dist

        for i, j in arr[temp]:
            if not visit[i]:
                visit[i] = True
                q.append((i, dist + j))

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))