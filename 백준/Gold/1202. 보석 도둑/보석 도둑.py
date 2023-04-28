import sys, heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
weight = [int(sys.stdin.readline()) for _ in range(K)]
weight.sort()
ans = 0
temp = []
for i in weight:
    while jew and i >= jew[0][0]:
        heapq.heappush(temp, - heapq.heappop(jew)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not jew:
        break
print(ans)