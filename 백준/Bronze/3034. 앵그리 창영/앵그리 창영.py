import math
import sys

N, W, H = map(int, sys.stdin.readline().split())
diagonal = math.sqrt(W**2 + H**2)

for _ in range(N):
    match = int(sys.stdin.readline())
    if match <= diagonal:
        print("DA")
    else:
        print("NE")
