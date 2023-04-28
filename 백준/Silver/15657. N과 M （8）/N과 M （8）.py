import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
s = []

def dfs(start):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(N):
        if start == 0 or s[start - 1] <= lst[i]:
            s.append(lst[i])
            dfs(start + 1)
            s.pop()

dfs(0)