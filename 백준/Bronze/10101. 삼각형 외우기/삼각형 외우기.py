import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
if A == B and B == C and C == 60:
    print("Equilateral")
elif A + B + C == 180:
    if A == B or B == C or C == A:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")