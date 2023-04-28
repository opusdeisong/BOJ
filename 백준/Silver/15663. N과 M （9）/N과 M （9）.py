import sys

N, M = map(int, sys.stdin.readline().split())
lst = list((map(int, sys.stdin.readline().split())))
visited = [False] * N
lst.sort()
s = []

def dfs():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    cnt = 0
    for i in range(len(lst)):
        if not visited[i] and cnt != lst[i]:
            visited[i] = True
            s.append(lst[i])
            cnt = lst[i]
            dfs()
            visited[i] = False
            s.pop()

dfs()