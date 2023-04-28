import sys

L, N, T = map(int, sys.stdin.readline().split())
list_R = []
list_L = []
cnt = 0
for _ in range(N):
    loc, side = map(str, sys.stdin.readline().split())
    loc = int(loc)
    if side == 'R': list_R.append(loc)
    if side == 'L': list_L.append(loc)
for _ in range(T):
    for i in range(len(list_R)):
        list_R[i] = list_R[i] + 1
    for i in range(len(list_L)):
        list_L[i] = list_L[i] - 1
    for i in list_R:
        if i in list_L:
            cnt += 1
    for i in list_R:
        if i == L:
            list_L.append(L)
            list_R.remove(L)
    for i in list_L:
        if i == 0:
            list_L.remove(0)
            list_R.append(0)
print(cnt)