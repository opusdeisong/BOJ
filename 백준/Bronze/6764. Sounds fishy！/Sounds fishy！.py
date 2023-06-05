import sys

depths = [int(sys.stdin.readline()) for _ in range(4)]

if all(x < y for x, y in zip(depths, depths[1:])):
    print("Fish Rising")
elif all(x > y for x, y in zip(depths, depths[1:])):
    print("Fish Diving")
elif all(x == y for x, y in zip(depths, depths[1:])):
    print("Fish At Constant Depth")
else:
    print("No Fish")