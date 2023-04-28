import sys, heapq

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
box.sort(key = lambda x: x[1])
truck = [C] * (N + 1)
cnt = 0

for i in range(M):
    temp = C
    for j in range(box[i][0], box[i][1]):
        if truck[j] < temp:
            temp = truck[j]
    temp = min(temp, box[i][2])
    cnt += temp
    for j in range(box[i][0], box[i][1]):
        truck[j] -= temp

print(cnt)
