import sys

P, K = map(int, sys.stdin.readline().split())
is_good = True
r = 0

for i in range(2, K):
    if P % i == 0:
        is_good = False
        r = i
        break

if is_good:
    print('GOOD')
else:
    print('BAD', r)
