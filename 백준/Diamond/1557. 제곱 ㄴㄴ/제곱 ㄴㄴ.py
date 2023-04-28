import sys
import math


def SFI_cnt(K):
    cnt = 0
    t = 1
    while t * t <= K:
        cnt += (temp[t] * (K // (t * t)))
        t += 1
    return cnt

K = int(sys.stdin.readline())

temp = [0 for i in range(45000)]
temp[1] = 1
i = 1
while i <= 44000:
    j = 2 * i
    while j <= 44000:
        temp[j] -= temp[i]
        j += i
    i += 1
f = 0
l = K * 2
while f < l - 1:
    m = (f + l) // 2
    if SFI_cnt(m) < K:
        f = m
    else:
        l = m
print(l)