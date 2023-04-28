import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
visited = [False] * N
s = []

def dfs():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(N):
        if not visited[i]:
            s.append(lst[i])
            visited[i] = True
            dfs()
            visited[i] = False
            s.pop()

dfs()