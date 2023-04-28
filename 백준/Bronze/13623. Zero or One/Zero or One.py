A, B, C = map(int, input().split())

if (A == 1 and B == 0 and C == 0) or (A == 0 and B == 1 and C == 1):
    print("A")
elif (A == 1 and B == 0 and C == 1) or (A == 0 and B == 1 and C == 0):
    print("B")
elif (A == 1 and B == 1 and C == 0) or (A == 0 and B == 0 and C == 1):
    print("C")
else:
    print("*")