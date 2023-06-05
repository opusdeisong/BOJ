import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())
Z = int(sys.stdin.readline())

if X + Y <= Z + 0.5:
    print(1)
else:
    print(0)
