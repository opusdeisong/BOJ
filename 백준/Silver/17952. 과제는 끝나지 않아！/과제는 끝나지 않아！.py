import sys
from collections import deque

dq = deque()
score = 0
for _ in range(int(sys.stdin.readline())):
    sub = list(map(int, sys.stdin.readline().split()))
    if dq == [] or sub[0] == 1:
        dq.append(sub[1:])
    if dq:
        dq[-1][1] -= 1
        if dq[-1][1] == 0:
            score += dq.pop()[0]

print(score)