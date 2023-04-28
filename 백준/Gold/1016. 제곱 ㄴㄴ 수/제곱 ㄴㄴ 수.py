import sys

min, max = map(int, sys.stdin.readline().split())

ans = max - min + 1
temp = [0 for i in range(max - min + 1 )]

for i in range(2, int(max ** 0.5 + 1)):
    square = i ** 2
    for j in range((((min - 1) // square) + 1) * square, max + 1, square):
        if not temp[j - min]:
            temp[j - min] = True
            ans -= 1
print(ans)