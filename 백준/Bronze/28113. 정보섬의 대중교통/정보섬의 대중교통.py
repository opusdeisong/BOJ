import sys

N, A, B = map(int, sys.stdin.readline().split())
if A>B:
    print("Subway")
elif A<B:
    print("Bus")
else:
    print("Anything")