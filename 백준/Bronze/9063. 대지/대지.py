import sys

N = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_x = min(points, key=lambda x: x[0])[0]
max_x = max(points, key=lambda x: x[0])[0]
min_y = min(points, key=lambda x: x[1])[1]
max_y = max(points, key=lambda x: x[1])[1]

area = (max_x - min_x) * (max_y - min_y)
print(area)
