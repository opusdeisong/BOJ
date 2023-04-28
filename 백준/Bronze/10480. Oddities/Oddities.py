T = int(input())


even = [10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]
for _ in range(T):
    N = int(input())
    if N in even:
        print(f"{N} is even")
    else:
        print(f"{N} is odd")