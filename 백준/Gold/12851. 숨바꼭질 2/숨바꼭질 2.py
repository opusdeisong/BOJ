import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100001
dist = [[0, -1] for _ in range(MAX)]
q = deque()
q.append(N)
dist[N][1] = 0
dist[N][0] = 1

while q:
    temp = q.popleft()
    if 0 <= temp - 1 < MAX:
        if dist[temp - 1][1] == -1:
            dist[temp - 1][1] = dist[temp][1] + 1
            q.append(temp - 1)
            dist[temp - 1][0] += dist[temp][0]
        elif dist[temp][1] + 1 == dist[temp - 1][1]:
            dist[temp - 1][0] += dist[temp][0]
    if temp * 2 < MAX:
        if dist[temp * 2][1] == -1:
            dist[temp * 2][1] = dist[temp][1] + 1
            q.append(temp * 2)
            dist[temp * 2][0] += dist[temp][0]
        elif dist[temp][1] + 1 == dist[temp * 2][1]:
            dist[temp * 2][0] += dist[temp][0]
    if temp + 1 < MAX:
        if dist[temp + 1][1] == -1:
            dist[temp + 1][1] = dist[temp][1] + 1
            q.append(temp + 1)
            dist[temp + 1][0] += dist[temp][0]
        elif dist[temp][1] + 1 == dist[temp + 1][1]:
            dist[temp + 1][0] += dist[temp][0]
print(dist[K][1])
print(dist[K][0])
