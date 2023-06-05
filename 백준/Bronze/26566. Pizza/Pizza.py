import sys

n = int(sys.stdin.readline())
for _ in range(n):
    A1, P1 = map(int, sys.stdin.readline().split())
    R1, P2 = map(int, input().split())
    slice_value = A1 / P1
    pizza_value = (3.1416 * R1 * R1) / P2
    if slice_value > pizza_value:
        print("Slice of pizza")
    else:
        print("Whole pizza")