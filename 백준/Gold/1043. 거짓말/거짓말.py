import sys

N, M = map(int, sys.stdin.readline().split())
truth = set(sys.stdin.readline().split()[1:])
parties = []

for _ in range(M):
    parties.append(set(sys.stdin.readline().split()[1:]))

for _ in range(M):
    for i in parties:
        if i & truth:
            truth = truth.union(i)

cnt = 0
for i in parties:
    if not (i & truth):
        cnt += 1

print(cnt)
