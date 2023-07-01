import sys

for _ in range(int(sys.stdin.readline())):
    points = []
    distances = []

    for i in range(4):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))

    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            distances.append(dx * dx + dy * dy)

    distances.sort()

    print(int(distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]))
