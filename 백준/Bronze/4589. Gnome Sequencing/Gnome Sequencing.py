import sys

N = int(sys.stdin.readline())
print('Gnomes:')
for _ in range(N):
    a, b, c = map(int, input().split())
    if a < b < c or a > b > c:
        print('Ordered')
    else:
        print('Unordered')
