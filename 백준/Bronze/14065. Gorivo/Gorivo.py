x = float(input())

liters_per_100_km = 100 / (x * 1.609344 / 3.785411784)

print('{:.6f}'.format(liters_per_100_km))
