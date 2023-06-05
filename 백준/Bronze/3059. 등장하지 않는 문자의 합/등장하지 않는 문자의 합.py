import sys

T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline()
    ascii_sum = 0

    for i in range(65, 91):
        if chr(i) not in S:
            ascii_sum += i

    print(ascii_sum)
