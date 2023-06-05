import sys, math

k, w, m = map(int, sys.stdin.readline().split())
hits = 0

print(math.ceil((w - k) / m))

