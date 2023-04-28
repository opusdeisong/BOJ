import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
in_degree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    in_degree[B] += 1
    graph[A].append(B)

q = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)
ans = []
while q:
    temp = heapq.heappop(q)
    ans.append(temp)
    for i in graph[temp]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            heapq.heappush(q, i)

print(*ans)