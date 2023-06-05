import sys

a, b, c = map(int, sys.stdin.readline().split())
sticks = [a, b, c]
sticks.sort()
if sticks[0] == sticks[1] == sticks[2]:
    print(2)
elif sticks[0]**2 + sticks[1]**2 == sticks[2]**2:
    print(1)
else:
    print(0)
