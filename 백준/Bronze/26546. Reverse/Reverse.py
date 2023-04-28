T = int(input())
for _ in range(T):
    a, b, c = map(str, input().split())
    b = int(b)
    c = int(c)
    for i in range(len(a)):
        if i < b or i >= c:
            print(a[i], end = "")
    print()