import sys

A_B = sys.stdin.readline().rstrip()
if '0' in A_B :
    if A_B == "1010":
        print(20)
    elif A_B[-1] == '0':
        print(int(A_B[0]) + 10)
    else:
        print(int(A_B[2]) + 10)
else:
    print(int(A_B[0]) + int(A_B[1]))