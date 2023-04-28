import sys

N, K = map(int, sys.stdin.readline().split())
ele = list(map(int, sys.stdin.readline().split()))

plug = []
ans = 0

for i in range(K):
    if ele[i] in plug:
        continue

    elif len(plug) != N:
        plug.append(ele[i])
        continue

    temp = 0
    tempp = 0

    for j in plug:
        if j not in ele[i:]:
            tempp = j
            break
        elif ele[i:].index(j) > temp:
            temp = ele[i:].index(j)
            tempp = j
    plug[plug.index(tempp)] = ele[i]
    ans += 1

print(ans)