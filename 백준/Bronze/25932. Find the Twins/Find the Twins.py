import sys

n = int(sys.stdin.readline())
for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    print(" ".join(map(str, numbers)))
    mack = 18 in numbers
    zack = 17 in numbers
    if mack and zack:
        print("both")
    elif mack:
        print("mack")
    elif zack:
        print("zack")
    else:
        print("none")
    print()
