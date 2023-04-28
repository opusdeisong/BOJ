import sys
from itertools import combinations

n,s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1, n + 1):
    com = combinations(arr, i)
    for x in com:
        if sum(x) == s:
            cnt += 1
print(cnt)