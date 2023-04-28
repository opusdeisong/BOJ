import sys

def ans(A, B, C):
    if B == 1: return A % C
    elif B % 2 == 0: return (ans(A, B // 2, C) ** 2) % C
    else: return ((ans(A, B // 2, C) ** 2) * A) % C

A, B, C = map(int, sys.stdin.readline().split())


print(ans(A, B, C))