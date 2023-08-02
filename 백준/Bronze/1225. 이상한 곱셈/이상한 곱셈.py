import sys

A, B = map(int, sys.stdin.readline().split())
temp = 0
while A > 0:
    temp += A % 10
    A //= 10
tempp = 0
while B > 0:
    tempp += B % 10
    B //= 10
print(temp * tempp)