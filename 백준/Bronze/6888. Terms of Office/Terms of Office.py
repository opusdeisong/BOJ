import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())
for i in range(Y - X + 1):
    if i % 60 == 0:
        print(f"All positions change in year {X + i}")