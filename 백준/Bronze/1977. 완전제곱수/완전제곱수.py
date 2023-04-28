from math import sqrt
M = int(input())
N = int(input())
list = []
for i in range(M, N + 1):
    if sqrt(i) % 1 == 0:
        list.append(i)
if len(list) == 0:
    print(-1)
    exit()
print(sum(list))
print(list[0])