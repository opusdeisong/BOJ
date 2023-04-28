import sys

N = int(sys.stdin.readline())

A, B, C, D = map(int, sys.stdin.readline().split())

a = A * N + B
b = C * N + D
if a == b:
    print(f"Yes {a}")
else:
    print("No")