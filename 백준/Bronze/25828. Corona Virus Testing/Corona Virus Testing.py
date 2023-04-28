g, p, t = map(int, input().split())
temp = g * p
tempp = g + t * p
if temp > tempp:
    print(2)
elif temp < tempp:
    print(1)
else:
    print(0)