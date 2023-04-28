import sys
T = int(sys.stdin.readline())
if T % 10 != 0:
    print(-1)
else:
    print(f"{T // 300} {(T % 300) // 60} {T % 60 // 10}")