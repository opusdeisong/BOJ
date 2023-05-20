import sys

N = int(input())
d = p = 0

for _ in range(N):
    winner = sys.stdin.readline().rstrip()
    if winner == 'D':
        d += 1
    else:
        p += 1
    if abs(d - p) >= 2:
        break

print(f"{d}:{p}")
