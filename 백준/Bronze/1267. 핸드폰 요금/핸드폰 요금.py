import sys

N = int(sys.stdin.readline())
call_times = list(map(int, sys.stdin.readline().split()))

Y, M = 0, 0
for time in call_times:
    Y += ((time // 30) + 1) * 10
    M += ((time // 60) + 1) * 15

if Y < M:
    print('Y', Y)
elif M < Y:
    print('M', M)
else:
    print('Y M', Y)
