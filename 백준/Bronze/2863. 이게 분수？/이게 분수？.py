import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

rotation_values = [A/C + B/D, C/D + A/B, D/B + C/A, B/A + D/C]
max_value = max(rotation_values)

print(rotation_values.index(max_value))
