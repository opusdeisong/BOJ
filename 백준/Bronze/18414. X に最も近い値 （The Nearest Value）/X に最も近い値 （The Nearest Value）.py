X, L, R = map(int, input().split())

if L <= X <= R:
    print(X)
elif X < L:
    print(L)
else:
    print(R)
