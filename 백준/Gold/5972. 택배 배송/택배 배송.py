import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = 1

visited = [float("inf")] * (V + 1)
route = [[] for _ in range(V + 1)]

visited[K] = 0
visited[0] = 0

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    route[u].append((v, w))
    route[v].append((u, w))

heap = [(0, K)]

while heap:
    w, v = heapq.heappop(heap)
    
    if visited[v] < w:
        continue
    
    for nv, nw in route[v]:
        new_weight = w + nw
        if new_weight < visited[nv]:
            visited[nv] = new_weight
            heapq.heappush(heap, (new_weight, nv))

print(visited[V])