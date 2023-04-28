import sys

N, Q = map(int, sys.stdin.readline().split())
one = [0 for i in range(2 * N)]
two = [0 for i in range(2 * N)]
three = [0 for i in range(2 * N)]


for i in range(1, N + 1):
    num = int(sys.stdin.readline())

    one[i] = one[i - 1]
    two[i] = two[i - 1]
    three[i] = three[i - 1]

    if num == 1:
        one[i] += 1
    elif num == 2:
        two[i] += 1
    elif num == 3:
        three[i] += 1


for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())

    print(f"{one[b] - one[a - 1]} {two[b] - two[a - 1]} {three[b] - three[a - 1]}")