import sys
temp = 1_000_000_007

def ans(N, S):
    return S * square(N, temp - 2) % temp

def square(n, e):
    if e == 1:
        return n % temp
    elif not (e % 2):
        h = square(n, e // 2)
        return h ** 2  % temp
    else:
        return n * square(n, e - 1) % temp
sum = 0
M = int(sys.stdin.readline())
for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())
    sum += ans(N, S)
    sum %= temp
print(sum)