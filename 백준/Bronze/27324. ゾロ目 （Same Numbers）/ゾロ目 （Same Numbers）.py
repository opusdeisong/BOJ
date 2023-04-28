N = int(input())
temp = N % 10
N = N // 10
if temp == N:
    print(1)
else:
    print(0)