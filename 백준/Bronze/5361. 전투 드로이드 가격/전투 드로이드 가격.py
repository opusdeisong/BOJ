import sys

T = int(sys.stdin.readline())
costs = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(T):
    parts = list(map(int, sys.stdin.readline().split()))
    total_cost = sum(p*c for p, c in zip(parts, costs))
    print(f"${total_cost:.2f}")
