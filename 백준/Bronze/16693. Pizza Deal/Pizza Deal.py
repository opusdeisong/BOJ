import math
import sys

A1, P1 = map(int, sys.stdin.readline().split())
R1, P2 = map(int, sys.stdin.readline().split())
pizza_slice_value = A1 / P1
whole_pizza_value = math.pi * R1**2 / P2
if pizza_slice_value > whole_pizza_value:
    print('Slice of pizza')
else:
    print('Whole pizza')
