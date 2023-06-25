import sys

INF = 9999999

def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

n, m, r = map(int, sys.stdin.readline().split())

item = [0] + [int(x) for x in sys.stdin.readline().split()]

arr = [[0 if i == j else INF for j in range(n+1)] for i in range(n+1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    arr[a][b] = l
    arr[b][a] = l

arr = floyd_warshall(arr, n)

result = 0

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if arr[i][j] <= m:
            temp += item[j]
    result = max(result, temp)

print(result)