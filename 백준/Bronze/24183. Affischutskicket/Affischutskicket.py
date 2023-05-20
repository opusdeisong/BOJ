import sys

a, b, c = map(int, sys.stdin.readline().split())

a = a * 229 * 324 * 2 * 0.000001
b = b * 297 * 420 * 2 * 0.000001
c = c * 210 * 297 * 0.000001
print(a + b + c)