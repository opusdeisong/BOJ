import sys

A, B, N = map(int, sys.stdin.readline().split())

ans = A % B
for i in range(N - 1):
    ans = (ans * 10) % B
print((ans * 10)//B)