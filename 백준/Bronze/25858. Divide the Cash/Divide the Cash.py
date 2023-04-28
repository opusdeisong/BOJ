n, d = map(int, input().split())
peop = []
for _ in range(n):
    peop.append(int(input()))
temp = d // sum(peop)
for i in peop:
    print(temp * i)