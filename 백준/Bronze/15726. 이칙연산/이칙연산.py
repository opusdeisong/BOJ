import sys

A, B, C = map(int, sys.stdin.readline().split())

if B < C:
    print(A *C // B )
else:
    print(A * B // C)