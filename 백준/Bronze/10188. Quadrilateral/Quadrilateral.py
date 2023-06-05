import sys

N = int(sys.stdin.readline())

for _ in range(N):
    length, width = map(int, input().split())

    if length > 20 or width > 20 or length < 1 or width < 1:
        print('Invalid dimensions')
        continue

    for i in range(width):
        print('X' * length)

    print()
