import sys


def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

graph = floyd_warshall(graph, N)

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        if graph[i][j] == float('inf') and graph[j][i] == float('inf'):
            cnt += 1
    print(cnt)
