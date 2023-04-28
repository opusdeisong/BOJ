import sys, heapq

N = int(sys.stdin.readline())
q = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, N):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])
print(len(room))