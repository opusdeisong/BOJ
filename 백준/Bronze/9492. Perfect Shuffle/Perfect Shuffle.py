import sys


while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    if N % 2 == 0:
        word = [0 for i in range(N)]

    else:
        word = [0 for i in range(N + 1)]

    for i in range(N):
        word[i] = str(sys.stdin.readline())

    first = word[:len(word) // 2]
    second = word[len(word) // 2:]
    for i in range(len(first)):
        print(first[i],end = "")
        if second[i] != 0:
            print(second[i], end = "")