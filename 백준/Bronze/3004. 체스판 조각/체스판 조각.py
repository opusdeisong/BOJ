import sys

N = int(sys.stdin.readline())

if N % 2 == 0:
    result = ((N // 2) + 1) ** 2
else:
    result = ((N // 2) + 1) * ((N // 2) + 2)

print(result)
