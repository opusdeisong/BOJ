import sys

p1, q1, p2, q2 = map(int, sys.stdin.readline().split())
ans = p1 / q1 * p2 / q2 / 2
if int(ans) == ans:
    print(1)
else:
    print(0)