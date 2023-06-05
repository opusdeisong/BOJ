import sys

sticks = sorted(list(map(int, sys.stdin.readline().split())))
if sticks[2] >= sticks[0] + sticks[1]:
    sticks[2] = sticks[0] + sticks[1] - 1
print(sum(sticks))
