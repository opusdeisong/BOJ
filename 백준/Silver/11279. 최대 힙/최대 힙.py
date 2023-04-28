import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)