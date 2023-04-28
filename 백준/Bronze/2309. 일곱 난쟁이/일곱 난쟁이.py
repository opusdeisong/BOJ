import sys
A = []
for _ in range(9):
    A.append(int(sys.stdin.readline()))
temp = sum(A) - 100
for i in range(8):
    for j in range(i, 9):
        if A[i] + A[j] == temp and i != j:
            a = A[i]
            b = A[j]
A.remove(a)
A.remove(b)
A.sort()
for i in A:
    print(i)