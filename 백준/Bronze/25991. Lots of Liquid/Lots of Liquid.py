import math

n = int(input())
c = list(map(float, input().split()))
total_volume = sum([x**3 for x in c])
side_length = math.pow(total_volume, 1/3)
print("{:.10f}".format(side_length))
