import sys

N, K = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
ans = []
for i in range(1, N):
    ans.append(height[i] - height[i - 1])

ans.sort(reverse=True)
print(sum(ans[K - 1:]))