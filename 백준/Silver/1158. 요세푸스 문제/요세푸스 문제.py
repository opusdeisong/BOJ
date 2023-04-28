import sys

N, K = map(int, sys.stdin.readline().split())
num = []
for i in range(N):
    num.append(i+1)
index = (K - 1) % len(num)
print(f"<{num[index]}", end = '')
num.pop(index)
while len(num) != 0:
    index += K - 1
    if index >= len(num):
        index %= len(num)
    print(f", {num[index]}", end = '')
    num.pop(index)
print(">", end = '')