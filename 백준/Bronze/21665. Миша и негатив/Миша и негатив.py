import sys

n, m = map(int, sys.stdin.readline().split())
original = [list(sys.stdin.readline()) for _ in range(n)]
_ = sys.stdin.readline()
converted = [list(sys.stdin.readline()) for _ in range(n)]

errors = 0
for i in range(n):
    for j in range(m):
        if (original[i][j] == 'B' and converted[i][j] != 'W') or \
           (original[i][j] == 'W' and converted[i][j] != 'B'):
            errors += 1

print(errors)
