list = []
for i in range(1, 1001):
    for j in range(i):
        list.append(i)

sum = 0
A, B = map(int, input().split())
for i in list[A - 1:B]:
    sum += i
print(sum)