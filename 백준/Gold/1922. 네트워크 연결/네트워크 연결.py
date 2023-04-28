import sys

def find(p):
    if p == root[p]:
        return p
    root[p] = find(root[p])
    return root[p]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
root=[i for i in range(N + 1)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
arr.sort(key = lambda  x : x[2])
ans = 0

for a, b, c in arr:
    ar = find(a)
    br = find(b)
    if ar != br:
        ans += c
        if ar < br:
            root[br] = ar
        else:
            root[ar] = br
print(ans)