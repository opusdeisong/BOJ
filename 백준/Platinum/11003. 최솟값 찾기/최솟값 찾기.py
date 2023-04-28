import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
dq = deque()

for i in range(N):
    while dq and dq[0][0] <= i - L:
        dq.popleft()
    while dq and dq[-1][1] >= A[i]:
        dq.pop()

    dq.append((i, A[i]))
    print(dq[0][1], end = " ")