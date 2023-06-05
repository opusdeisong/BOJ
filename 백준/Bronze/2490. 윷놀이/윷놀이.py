import sys

for _ in range(3):
    a = list(map(int, sys.stdin.readline().split()))
    a = sum(a)
    if a == 0:
        print('D')
    elif a == 1:
        print('C')
    elif a == 2:
        print('B')
    elif a == 3:
        print('A')
    else:
        print('E')