import sys, heapq

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
co = list(map(int,sys.stdin.readline().split()))
co.sort()
dist = [co[i] - co[i - 1] for i in range(1, N)]
dist.sort(reverse=True)
if N > K:
    print(sum(dist[K - 1:]))
else:
    print(0)