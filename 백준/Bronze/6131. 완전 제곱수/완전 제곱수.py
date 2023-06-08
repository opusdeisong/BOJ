import sys

N = int(sys.stdin.readline())
count = 0
for i in range(1, 501):
    for j in range(i, 501):
        if j ** 2 - i ** 2 == N:
            count += 1
print(count)
