import sys

N = int(sys.stdin.readline())

total_cost = 0

for _ in range(N):
    H, B, K = map(int, sys.stdin.readline().split())

    if B > H:
        total_cost += (B - H) * K

print(total_cost)
