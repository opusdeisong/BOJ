import sys
from math import ceil

R, C, N = map(int, sys.stdin.readline().split())

rows = ceil(R / N)
columns = ceil(C / N)

print(rows * columns)