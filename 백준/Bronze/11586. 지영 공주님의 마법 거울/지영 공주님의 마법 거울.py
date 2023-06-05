import sys

N = int(sys.stdin.readline())
mirror = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
K = int(sys.stdin.readline())

if K == 1:
    for i in mirror:
        print(''.join(i))
elif K == 2:
    for i in mirror:
        print(''.join(i[::-1]))
elif K == 3:
    for i in mirror[::-1]:
        print(''.join(i))
