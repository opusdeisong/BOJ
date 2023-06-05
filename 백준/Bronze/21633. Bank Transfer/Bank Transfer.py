import sys

k = int(sys.stdin.readline())
ans = max(100, min(2000, k * 0.01 + 25))
print(f'{ans:.2f}')
