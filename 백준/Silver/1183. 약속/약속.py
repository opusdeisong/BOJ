import sys

N = int(sys.stdin.readline())
num = [0 for z in range(N)]
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    num[i] = B - A

num.sort()
ans = 0

if len(num) % 2 == 0:
    s = (len(num) // 2) - 1
    ans = num[s + 1] - num[s] + 1
else:
    ans = 1

print(ans)