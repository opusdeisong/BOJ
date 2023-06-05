import sys

A, B = map(int, sys.stdin.readline().split())

max_val = max(A+B, A-B)
min_val = min(A+B, A-B)

print(max_val)
print(min_val)
