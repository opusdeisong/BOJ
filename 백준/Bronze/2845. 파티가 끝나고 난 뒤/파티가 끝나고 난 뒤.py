a, b = map(int, input().split())
p = list(map(int, input().split()))
pa = a * b
for i in p:
    print(i - pa, end=' ')