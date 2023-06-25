import sys


def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


V, E = map(int, sys.stdin.readline().split())

matrix = [[float('inf')] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    x, y, c = map(int, sys.stdin.readline().split())
    matrix[x][y] = c

matrix = floyd_warshall(matrix, V)

answer = float('inf')
for i in range(1, V + 1):
    answer = min(answer, matrix[i][i])

if answer == float('inf'):
    print(-1)
else:
    print(answer)
