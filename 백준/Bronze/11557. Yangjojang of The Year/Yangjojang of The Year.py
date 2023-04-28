T = int(input())
for i in range(T):
    N = int(input())
    univ = {}
    for j in range(N):
        A, B = input().split()
        univ[int(B)] = A
    print(univ[max(univ)])