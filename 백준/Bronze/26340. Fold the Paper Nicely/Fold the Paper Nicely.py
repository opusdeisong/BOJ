import sys

n = int(sys.stdin.readline())

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    print("Data set:", *data)

    width, height, folds = data

    for _ in range(folds):
        if width > height:
            width = width // 2
        else:
            height = height // 2

    print(max(width, height), min(width, height))
    print()
