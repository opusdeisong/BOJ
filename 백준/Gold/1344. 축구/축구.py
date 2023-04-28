import sys

A = int(sys.stdin.readline())

B = int(sys.stdin.readline())

C = [2, 3, 5, 7, 11, 13, 17]
D =[153, 816, 8568, 31824, 31824, 8568, 18]

PA = A / 100.0
PB = B / 100.0
SA = 0
SB = 0

for i in range(7):
    SA += D[i] * pow(PA, C[i]) * pow(1.0 - PA, 18 - C[i])
    SB += D[i] * pow(PB, C[i]) * pow(1.0 - PB, 18 - C[i])

print(SA + SB - SA * SB)

