import sys
N, M = map(int, sys.stdin.readline().split())

A = set()
for i in range(N):
    A.add(sys.stdin.readline())

B = set()
for i in range(M):
    B.add(sys.stdin.readline())

result = sorted(list(A & B))

print(len(result))

for i in result:
    print(i, end="")