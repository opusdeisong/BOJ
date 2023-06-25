import sys

INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    from_vertex, to_vertex, weight = map(int, sys.stdin.readline().split())
    graph[from_vertex-1][to_vertex-1] = min(graph[from_vertex-1][to_vertex-1], weight)

graph = floyd_warshall(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
