import sys

prev_temp = float(sys.stdin.readline())
while True:
    cur_temp = float(sys.stdin.readline())
    if cur_temp == 999:
        break
    print(f"{cur_temp - prev_temp:.2f}")
    prev_temp = cur_temp
