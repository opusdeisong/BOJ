import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    candies = list(map(int, sys.stdin.readline().split()))
    children = sum([candy // K for candy in candies])
    print(children)
