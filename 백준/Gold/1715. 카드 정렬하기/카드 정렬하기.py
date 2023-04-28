import sys, heapq

N = int(sys.stdin.readline())
card = []
for i in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

ans = 0
while len(card) != 1:
    temp = heapq.heappop(card) + heapq.heappop(card)
    ans += temp
    heapq.heappush(card, temp)

print(ans)