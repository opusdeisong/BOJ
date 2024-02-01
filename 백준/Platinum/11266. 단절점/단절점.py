import sys
sys.setrecursionlimit(10 ** 6)
def dfs(node, root, cnt):
    visit[node] = cnt = cnt + 1
    ret = visit[node]
    child = 0

    for next_node in graph[node]:
        if visit[next_node]:
            ret = min(ret, visit[next_node])
            continue

        child += 1
        prev = dfs(next_node, False, cnt)
        if not root and prev >= visit[node]:
            cut[node] = True

        ret = min(ret, prev)

    if root and child > 1:
        cut[node] = True

    return ret

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]
visit = [0] * (node + 1)
cut = [False] * (node + 1)
cnt = 0

for _ in range(edge):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, node + 1):
    if not visit[i]:
        dfs(i, True, cnt)

ans = [i for i in range(1, node + 1) if cut[i]]
print(len(ans))
print(' '.join(map(str, ans)))