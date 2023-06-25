import sys


def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif graph[i][k] != 0 and graph[k][j] != 0:
                    if graph[i][j] == 0:
                        graph[i][j] = graph[i][k] + graph[k][j]
                    else:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

n, m = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = graph[y-1][x-1] = 1

graph = floyd_warshall(graph)

result = float('inf')
person = None

for i in range(n):
    sum_paths = sum(graph[i][j] for j in range(n))

    if sum_paths < result:
        result = sum_paths
        person = i + 1
print(person)
