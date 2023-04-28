import sys
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    num = [1] * 10
    for j in range(1, n):
        temp = num.copy()
        num[0] = temp[7]
        num[1] = temp[2] + temp[4]
        num[2] = temp[1] + temp[3] + temp[5]
        num[3] = temp[2] + temp[6]
        num[4] = temp[1] + temp[7] + temp[5]
        num[5] = temp[2] + temp[4] + temp[6] + temp[8]
        num[6] = temp[9] + temp[3] + temp[5]
        num[7] = temp[4] + temp[8] + temp[0]
        num[8] = temp[5] + temp[7] + temp[9]
        num[9] = temp[8] + temp[6]
    print(sum(num) % 1234567)