import sys

N = int(sys.stdin.readline())
cnt = 0
for i in range(1, N + 1):
    cnt += 1

    if i == N:
        print(cnt)
    if '50' in str(i):
        cnt += 1