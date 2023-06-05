import sys

T = int(sys.stdin.readline())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    F = E - V + 2
    print(F)
