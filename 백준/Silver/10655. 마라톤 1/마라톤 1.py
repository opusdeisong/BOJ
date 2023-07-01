import sys
#
n = int(sys.stdin.readline())
cx, cy = map(int, sys.stdin.readline().split())

points = [(cx, cy)]

total = 0
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    points.append((a, b))
    total += abs(cx - a) + abs(cy - b)
    cx, cy = a, b

ans = total

skip = 0

for i in range(1, n-1):
    prev_x, prev_y = points[i-1]
    cur_x, cur_y = points[i]
    next_x, next_y = points[i+1]

    dist = abs(prev_x - cur_x) + abs(prev_y - cur_y) + abs(cur_x - next_x) + abs(cur_y - next_y)

    straight = abs(prev_x - next_x) + abs(prev_y - next_y)

    skip = max(skip, dist - straight)

print(total - skip)
