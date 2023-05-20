import sys

t1, m1, t2, m2 = map(int, sys.stdin.readline().split())

if (t1 * 60 + m1) > (t2 * 60 + m2):
    t2 += 24

print(t2 * 60 + m2 - t1 * 60 - m1, (t2 * 60 + m2 - t1 * 60 - m1) // 30)