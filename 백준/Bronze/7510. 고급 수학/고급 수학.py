import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    sides = list(map(int, sys.stdin.readline().split()))
    sides.sort()
    print(f"Scenario #{i}:")
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("yes")
    else:
        print("no")
    print()
