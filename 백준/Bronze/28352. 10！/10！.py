import math
import sys


N = int(sys.stdin.readline())
factorial = math.factorial(N)

seconds_in_week = 7 * 24 * 60 * 60

weeks = factorial // seconds_in_week

print(weeks)