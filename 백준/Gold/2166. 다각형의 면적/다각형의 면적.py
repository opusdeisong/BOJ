import sys

N = int(sys.stdin.readline())
num = [0 for i in range(N)]
for _ in range(N):
    num[_] = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(N):
    if i == N - 1:
        ans = ans + num[i][0] * num[0][1] - num[i][1] * num[0][0]
    else:
        ans = ans + num[i][0] * num[i + 1][1] - num[i][1] * num[i + 1][0]
print(abs(ans / 2))