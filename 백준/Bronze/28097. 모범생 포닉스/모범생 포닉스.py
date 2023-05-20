import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
ans = sum(list) + (len(list) - 1) * 8
print(f"{ans // 24} {ans % 24}")