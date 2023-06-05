import sys

x, y = map(int, sys.stdin.readline().split())
x-=1
y-=1
dx = abs(x // 4 - y // 4)
dy = abs(x % 4 - y % 4)

result = dx + dy

print(result)