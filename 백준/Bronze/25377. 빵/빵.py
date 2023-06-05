import sys

N = int(sys.stdin.readline())
ans = 1001
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    if A <= B:
        ans = min(ans, B)
if ans == 1001:
    ans = -1
print(ans)