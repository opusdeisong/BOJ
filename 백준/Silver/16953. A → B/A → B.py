import sys

A, B = map(int, sys.stdin.readline().split())
trial = 1
while B != A:
    trial += 1
    temp = B
    if B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2

    if temp == B:
        trial = -1
        break
print(trial)