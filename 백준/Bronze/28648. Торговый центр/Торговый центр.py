n = int(input())
arrival_times = []

for _ in range(n):
    t, l = map(int, input().split())
    arrival_times.append(t + l)

print(min(arrival_times))
