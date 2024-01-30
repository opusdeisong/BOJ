import sys
sys.setrecursionlimit(10 ** 9)

def dfs(node):
    visited[node] = True
    no_early, with_early = 0, 1

    for conn in graph[node]:
        if not visited[conn]:
            dfs(conn)
            no_early += early[conn]
            with_early += min(no_early_adopter[conn], early[conn])

    no_early_adopter[node], early[node] = no_early, with_early

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
no_early_adopter, early = [0] * (n + 1), [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(no_early_adopter[1], early[1]))
