import sys
N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort()

closest_dist = (points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2

for idx in range(N):
    sqrt_dist = closest_dist ** 0.5

    for i in range(idx - 1, -1, -1):
        if (points[idx][0] - points[i][0]) < sqrt_dist:
            d = (points[idx][0] - points[i][0]) ** 2 + (points[idx][1] - points[i][1]) ** 2

            if d < closest_dist:
                closest_dist = d
        else:
            break

    for i in range(idx + 1, len(points)):
        if (points[i][0] - points[idx][0]) < sqrt_dist:
            d = (points[idx][0] - points[i][0]) ** 2 + (points[idx][1] - points[i][1]) ** 2

            if d < closest_dist:
                closest_dist = d
        else:
            break

print(closest_dist)
