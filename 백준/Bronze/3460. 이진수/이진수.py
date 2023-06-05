T = int(input())
for _ in range(T):
    n = int(input())
    binary = format(n, "b")
    for i in range(len(binary)):
        if binary[-i-1] == '1':
            print(i, end=' ')
    print()
