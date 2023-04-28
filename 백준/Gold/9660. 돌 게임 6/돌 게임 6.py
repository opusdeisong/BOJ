import sys

N = int(sys.stdin.readline())
if N % 7 == 2 or N % 7 == 0:
    print("CY")
else:
    print("SK")