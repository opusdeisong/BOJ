import sys

T = int(sys.stdin.readline())

for _ in range(T):
    size = int(sys.stdin.readline())
    box = [['#']*size for _ in range(size)]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            box[i][j] = 'J'
    print('\n'.join(''.join(row) for row in box))
    print()
