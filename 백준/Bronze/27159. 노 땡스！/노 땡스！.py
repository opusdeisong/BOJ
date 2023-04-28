import sys
N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
sum = 0
temp = list[0]
streak = 0
if N == 1:
    print(list[0])
else:
    for i in range(1, len(list)):
        if temp == list[i] - 1 - streak:
            streak += 1
            if i == len(list) - 1:
                sum += temp
        else:
            sum += temp
            temp = list[i]
            streak = 0
            if i == len(list) - 1:
                sum += temp
    print(sum)