import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(N):
    if students[i] != i + 1:
        cnt += 1

print(cnt)
