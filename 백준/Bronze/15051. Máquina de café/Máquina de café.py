A1 = int(input())
A2 = int(input())
A3 = int(input())

time1 = A2 * 2 + A3 * 4
time2 = A1 * 2 + A3 * 2
time3 = A1 * 4 + A2 * 2

min_time = min(time1, time2, time3)

print(min_time)
