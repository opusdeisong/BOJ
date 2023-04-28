import sys


def SFI_cnt(K):
    cnt = 0
    t = 1
    while t * t <= K:
        cnt += (temp[t] * (K // (t * t)))
        t += 1
    return cnt

K = int(sys.stdin.readline())

temp = [0 for _ in range(1000001)]
temp[1] = 1
i = 1
while i <= 1000000:
    if temp[i]:
        j = 2 * i
        while j <= 1000000:
            temp[j] -= temp[i]
            j += i
    i += 1
f = 0
l = 10 ** 11
while f < l - 1:
    m = (f + l) // 2
    if m - SFI_cnt(m) < K:
        f = m
    else:
        l = m
print(l)