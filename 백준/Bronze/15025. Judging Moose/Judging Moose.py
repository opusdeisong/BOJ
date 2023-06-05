import sys

l, r = map(int, sys.stdin.readline().split())
if l == r:
    if l == 0:
        print("Not a moose")
    else:
        print("Even", l*2)
else:
    print("Odd", max(l, r)*2)
