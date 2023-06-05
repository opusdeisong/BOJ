import math
import sys

N, A, B, C, D = map(int, sys.stdin.readline().split())

set_x = B * math.ceil(N / A)
set_y = D * math.ceil(N / C)

print(min(set_x, set_y))