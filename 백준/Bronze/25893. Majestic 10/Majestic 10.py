import sys

n = int(sys.stdin.readline())
for _ in range(n):
    stats = list(map(int, sys.stdin.readline().split()))
    print(' '.join(map(str, stats)))
    doubles = sum([1 for stat in stats if stat >= 10])
    if doubles == 0:
        print('zilch')
    elif doubles == 1:
        print('double')
    elif doubles == 2:
        print('double-double')
    else:
        print('triple-double')
    print()
