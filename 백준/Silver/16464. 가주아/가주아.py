import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    if math.log2(K) % 1 == 0:
        print("GoHanGang")
    else:
        print("Gazua")