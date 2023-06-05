import sys


def time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

start_time = sys.stdin.readline().rstrip()
end_time = sys.stdin.readline().rstrip()

start_seconds = time_to_seconds(start_time)
end_seconds = time_to_seconds(end_time)

if end_seconds >= start_seconds:
    print(end_seconds - start_seconds)
else:
    print(24*3600 - start_seconds + end_seconds)
