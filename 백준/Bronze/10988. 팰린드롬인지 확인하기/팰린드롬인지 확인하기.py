A = input()
new_A = ""
num = len(A)
while num > 0:
    new_A += A[num - 1]
    num -= 1
if new_A == A:
    print(1)
else:
    print(0)