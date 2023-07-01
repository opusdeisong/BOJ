import sys

k = int(sys.stdin.readline())
lengths = []

for i in range(6):
    d, l = map(int, sys.stdin.readline().split())
    lengths.append((d, l))

lengths.extend(lengths)

big_area = 0
small_area = 0

for i in range(3, 12):
    if lengths[i][0] == lengths[i - 2][0] and lengths[i - 1][0] == lengths[i - 3][0]:
        big_area = lengths[i + 1][1] * lengths[i + 2][1]
        small_area = lengths[i - 1][1] * lengths[i - 2][1]
        break

print(k * (big_area - small_area))
