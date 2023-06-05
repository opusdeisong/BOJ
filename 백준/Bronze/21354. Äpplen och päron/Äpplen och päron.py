import sys

A, P = map(int, sys.stdin.readline().split())
Axel = A * 7
Petra = P * 13

if Axel > Petra:
    print("Axel")
elif Axel < Petra:
    print("Petra")
else:
    print("lika")
