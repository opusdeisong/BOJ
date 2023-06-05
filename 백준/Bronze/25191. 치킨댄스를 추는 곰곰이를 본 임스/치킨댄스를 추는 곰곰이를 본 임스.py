import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())

ans = min(N, A // 2 + B)

print(ans)