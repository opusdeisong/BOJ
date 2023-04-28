import sys

N = int(sys.stdin.readline())
ans = ['CY', 'SK', 'CY', 'SK', 'SK']
print(ans[N % 5])