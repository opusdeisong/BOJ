import sys

N, M = map(int, sys.stdin.readline().split())
helmets = list(map(int, sys.stdin.readline().split()))
vests = list(map(int, sys.stdin.readline().split()))

max_helmet = max(helmets)
max_vest = max(vests)

print(max_helmet + max_vest)
