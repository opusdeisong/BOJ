import sys, heapq

N = int(sys.stdin.readline())
univ = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
univ.sort(key = lambda x: (x[1]))
ans=[]

for i in univ:
  heapq.heappush(ans, i[0])
  if len(ans) > i[1]:
    heapq.heappop(ans)

print(sum(ans))