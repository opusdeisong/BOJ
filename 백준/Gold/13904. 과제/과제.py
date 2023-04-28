import sys, heapq

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(reverse=True, key = lambda x : x[1])
ans = [0 for _ in range(1000)]
for i in range(N, 0, -1):
    for j in range(N):
        if arr[j][0] >= i:
            ans[i] = arr[j][1]
            arr[j][0] = 0
            break
print(sum(ans))