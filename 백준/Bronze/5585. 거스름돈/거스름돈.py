import sys

N = int(sys.stdin.readline())
N = 1000 - N
ans = 0
list = [500, 100, 50, 10, 5, 1]
for i in list:
    ans += N // i
    N = N % i
    if N == 0:
        break
print(ans)
