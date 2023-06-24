import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque([(N, 0)])
check = [False] * 1000001
parent = [0] * 1000001
path = []

while q:
    x, time = q.popleft()
    check[x] = True

    if x == K:
        idx = x
        while idx != N:
            path.append(idx)
            idx = parent[idx]
        print(time)
        break

    if 0 <= x - 1 <= 200000 and not check[x - 1]:
        q.append((x - 1, time + 1))
        check[x - 1] = True
        parent[x - 1] = x

    if 0 <= x + 1 <= 200000 and not check[x + 1]:
        q.append((x + 1, time + 1))
        check[x + 1] = True
        parent[x + 1] = x

    if 0 <= x * 2 <= 200000 and not check[x * 2]:
        q.append((x * 2, time + 1))
        check[x * 2] = True
        parent[x * 2] = x

print(N, end=' ')

for i in reversed(path):
    print(i, end=' ')
