N, L = map(int, input().split())
for i in range(L, 101):
    X = N - (i ** 2 + i) / 2
    if X % i == 0:
        X = int(X / i)
        if X >= -1:
            for j in range(1, i + 1):
                print(X + j, end =" ")
            break
else:
    print(-1)