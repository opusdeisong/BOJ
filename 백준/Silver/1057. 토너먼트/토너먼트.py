import sys

N, a, b = map(int, sys.stdin.readline().split())

cnt = 0

while (a != b):
    a = a - a // 2
    b = b - b // 2
    cnt += 1
print(cnt)