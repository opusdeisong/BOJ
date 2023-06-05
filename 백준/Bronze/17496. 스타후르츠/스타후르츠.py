import sys

N, T, C, P = map(int, sys.stdin.readline().split())
profit = ((N - 1) // T) * C * P
print(profit)
