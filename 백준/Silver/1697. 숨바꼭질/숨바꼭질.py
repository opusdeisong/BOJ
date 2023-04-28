import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100001
dist = [-1 for _ in range(MAX)]

q = deque()
q.append(N)
dist[N] = 0

while q:
    temp = q.popleft()
    if temp == K:
        break
    if 0 <= temp - 1 and dist[temp - 1] == -1:
        dist[temp - 1] = dist[temp] + 1
        q.append(temp - 1)
    if temp * 2 < 100001 and dist[temp * 2] == -1:
        dist[temp * 2] = dist[temp] + 1
        q.append(temp * 2)
    if temp + 1 < 100001 and dist[temp + 1] == - 1:
        dist[temp + 1] = dist[temp] + 1
        q.append(temp + 1)
print(dist[K])
