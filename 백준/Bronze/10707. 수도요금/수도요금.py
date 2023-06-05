import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

X_fee = A * P
if P <= C:
    Y_fee = B
else:
    Y_fee = B + D * (P - C)

print(min(X_fee, Y_fee))
