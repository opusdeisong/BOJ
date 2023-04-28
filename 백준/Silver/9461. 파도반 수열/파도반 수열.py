import sys
T = int(sys.stdin.readline())
list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10,101):
    list.append(list[i - 1] + list[i - 5])
for _ in range(T):
    N = int(sys.stdin.readline())
    print(list[N - 1])