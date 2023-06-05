import sys

start_time = (11 - 11) * 24 * 60 + 11 * 60 + 11

D, H, M = map(int, sys.stdin.readline().split())

end_time = (D - 11) * 24 * 60 + H * 60 + M

spent_time = end_time - start_time

if spent_time < 0:
    print(-1)
else:
    print(spent_time)