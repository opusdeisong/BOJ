import sys
chess = [1, 1, 2, 2, 2, 8]
A, B, C, D, E, F = map(int, sys.stdin.readline().split())
print(chess[0] - A, chess[1] - B, chess[2] - C, chess[3] - D, chess[4] - E, chess[5] - F)