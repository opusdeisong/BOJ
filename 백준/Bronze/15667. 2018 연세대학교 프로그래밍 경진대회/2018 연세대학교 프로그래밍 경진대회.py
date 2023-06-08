import sys

N = int(sys.stdin.readline())
K = 1

while K**2 + K + 1 <= N:
    K += 1

print(K - 1)
