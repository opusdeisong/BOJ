import heapq, sys

waiting_intervals = []
for _ in range(int(sys.stdin.readline())):
    start_point, end_point = map(int, sys.stdin.readline().split())
    if start_point > end_point:
        start_point, end_point = end_point, start_point
    waiting_intervals.append((start_point, end_point))

waiting_intervals.sort(key=lambda x: (x[1], x[0]))

rail_length = int(input())

waiting_queue = []
current_load = 0
max_capacity = 0

for interval in waiting_intervals:
    valid_start = interval[1] - rail_length

    while waiting_queue and waiting_queue[0] < valid_start:
        current_load -= 1
        heapq.heappop(waiting_queue)

    if interval[0] >= valid_start:
        current_load += 1
        heapq.heappush(waiting_queue, interval[0])
        max_capacity = max(max_capacity, current_load)

print(max_capacity)
