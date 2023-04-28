T = int(input())


for i in range(T):
    A = input().split()
    num = float(A[0])
    A.remove(A[0])
    for j in A:
        if j == "@":
            num *= 3
        elif j == "%":
            num += 5
        elif j == "#":
            num -= 7
    print(f"{num:.2f}")