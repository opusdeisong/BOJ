import sys

a, operator, b, _, c = sys.stdin.readline().split()

result = int(a) + int(b)

if result == int(c):
    print("YES")
else:
    print("NO")