import sys

a, b, c = map(int, sys.stdin.readline().split())
arr = [a + b, b + c, c + a]
arr2 = [a * b, b * c, c * a]
if a in arr or b in arr or c in arr:
    print(1)
elif a in arr2 or b in arr2 or c in arr2:
    print(2)
else:
    print(3)