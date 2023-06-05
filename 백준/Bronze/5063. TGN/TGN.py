import sys

N = int(sys.stdin.readline())
for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().split())
    if r < e - c:
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")
