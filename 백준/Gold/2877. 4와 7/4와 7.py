import sys

N = int(sys.stdin.readline()) + 1
ans = []
while N != 0:
    returnBinary = N % 2
    ans.append(returnBinary)
    N //= 2

ans.reverse()
ans.pop(0)

for digit in ans:
    if digit == 1:
        print("7", end="")
    else:
        print("4", end="")