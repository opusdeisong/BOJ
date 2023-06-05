import sys

M, S, G = map(int, sys.stdin.readline().split())
A, B = map(float, sys.stdin.readline().split())
L, R = map(int, sys.stdin.readline().split())

time_left = L/A + M/G
time_right = R/B + M/S

if time_left < time_right:
    print("friskus")
else:
    print("latmask")