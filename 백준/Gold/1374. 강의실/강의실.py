import sys, heapq

N = int(sys.stdin.readline())
lec = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lec.sort(key = lambda x:x[1])

min_heap = []
cnt = 0

for i in lec:
    while min_heap and min_heap[0] <= i[1]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, i[2])
    cnt = max(cnt, len(min_heap))

print(cnt)