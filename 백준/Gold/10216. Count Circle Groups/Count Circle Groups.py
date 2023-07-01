import sys

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    circles = []
    parent = list(range(num))
    result = num

    for i in range(num):
        x, y, r = map(int, sys.stdin.readline().split())
        circles.append((x, y, r))

    for i in range(num - 1):
        for j in range(i + 1, num):
            fx, fy, fr = circles[i]
            sx, sy, sr = circles[j]
            d1 = (fr + sr) ** 2
            d2 = (fx - sx) ** 2 + (fy - sy) ** 2

            p_i = i
            while parent[p_i] != p_i:
                p_i = parent[p_i]
            p_j = j
            while parent[p_j] != p_j:
                p_j = parent[p_j]

            if d1 >= d2 and p_i != p_j:
                parent[p_i] = p_j
                result -= 1

    print(result)
