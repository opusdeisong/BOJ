import sys, heapq

N = int(sys.stdin.readline())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
room.sort()
cnt = 1
ans = [0]

for s, e in room:
    if s >= ans[0]:
        heapq.heappop(ans)
    else:
        cnt += 1
    heapq.heappush(ans, e)
print(cnt)