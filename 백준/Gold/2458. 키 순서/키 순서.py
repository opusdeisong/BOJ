import sys

INF = 9999999

def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

N, M = map(int, sys.stdin.readline().split())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

graph = floyd_warshall(graph, N)

ans = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N - 1:
        ans += 1

print(ans)
