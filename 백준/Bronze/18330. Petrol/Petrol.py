import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
ans = min(k + 60, n) * 1500 + (n - min(k + 60, n)) * 3000
print(ans)