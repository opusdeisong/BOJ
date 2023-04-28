T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    a, b = A, B
    while b != 0:
        temp = b
        b = a % b
        a = temp

    print(f"{(A * B) // a}")
