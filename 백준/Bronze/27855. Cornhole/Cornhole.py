import sys

H1, B1 = map(int, sys.stdin.readline().split())
H2, B2 = map(int, sys.stdin.readline().split())
a = H1 * 3 + B1
b = H2 * 3 + B2
if a == b:
    print("NO SCORE")
elif a > b:
    print(f"{1} {a - b}")
else:
    print(f"{2} {b - a}")