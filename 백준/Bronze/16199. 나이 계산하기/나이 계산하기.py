import sys

by, bm, bd = map(int, sys.stdin.readline().split())
cy, cm, cd = map(int, sys.stdin.readline().split())

if cm > bm or (cm == bm and cd >= bd):
    man_age = cy - by
else:
    man_age = cy - by - 1

korean_age = cy - by + 1

year_age = cy - by

print(man_age)
print(korean_age)
print(year_age)