import sys

N = int(sys.stdin.readline())
milk = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(N):
    if milk[i] == cnt % 3:
        cnt += 1
print(cnt)