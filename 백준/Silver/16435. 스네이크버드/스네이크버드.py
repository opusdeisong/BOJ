import sys

N, L = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
h.sort()
for i in h:
    if i > L:
        break
    else:
        L += 1
print(L)