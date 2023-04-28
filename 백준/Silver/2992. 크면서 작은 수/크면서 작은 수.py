import sys

N = int(sys.stdin.readline())
ans = N
num = []

while N > 0:
    num.append(N % 10)
    N = N // 10

num.sort()
M = 0

for i in range(ans + 1, 1000001):
    temp = []
    M = i
    while M > 0:
        temp.append(M % 10)
        M = M // 10
    temp.sort()
    if num == temp:
        print(i)
        break

if i == 1000000:
    print(0)