import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(f"Pairs for {n}:",end ='')
    cnt = 0
    for i in range(1, n//2 + 1):
        if i < n - i:
            if cnt >= 1:
                print(",", end='')
            print(f" {i} {n - i}", end='')
            cnt += 1
    print()