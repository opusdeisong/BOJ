import sys

A, B = map(int, sys.stdin.readline().split())
print(min(A // 2, B))