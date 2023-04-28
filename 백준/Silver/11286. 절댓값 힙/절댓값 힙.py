import sys, heapq

T = int(sys.stdin.readline())

heap = []
for _ in range(T):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(temp), temp))