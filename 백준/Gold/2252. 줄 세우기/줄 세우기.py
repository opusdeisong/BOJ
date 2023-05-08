import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

inDegree = [ 0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
queue = deque()

for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    inDegree[B] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    for i in graph[student]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)
    print(student, end = ' ')