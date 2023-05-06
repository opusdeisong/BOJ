import sys
arr = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())
if x in arr:
    print(arr.index(x) + 1)
else:
    print(0)