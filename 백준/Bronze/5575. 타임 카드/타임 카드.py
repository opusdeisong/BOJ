import sys

times = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

for time in times:
    st = time[0] * 3600 + time[1] * 60 + time[2]
    et = time[3] * 3600 + time[4] * 60 + time[5]
    ans = et - st
    print(f"{ans // 3600} {(ans % 3600) // 60} {ans % 60}")