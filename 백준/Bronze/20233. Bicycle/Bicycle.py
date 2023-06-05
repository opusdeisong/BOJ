import sys

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
T = int(sys.stdin.readline())

cost_a = a + max(0, T - 30) * x * 21
cost_b = b + max(0, T - 45) * y * 21

print(cost_a, cost_b)
