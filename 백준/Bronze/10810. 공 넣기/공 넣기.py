import sys

N, M = map(int, sys.stdin.readline().split())

buckets = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    buckets[i-1:j] = [k]*(j-i+1)

print(' '.join(map(str, buckets)))
