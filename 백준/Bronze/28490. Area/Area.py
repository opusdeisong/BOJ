import sys

ans = 0

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    temp = a * b
    ans = max(ans, temp)

print(ans)