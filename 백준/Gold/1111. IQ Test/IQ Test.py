N = int(input())
data = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if data[0] == data[1]:
        print(data[0])
    else:
        print("A")
else:
    if data[0] == data[1]:
        A = 0
    else:
        A = (data[1] - data[2]) // (data[0] - data[1])
    B = data[1] - data[0] * A
    for i in range(N - 1):
        expect = data[i] * A + B
        if data[i + 1] != expect:
            print("B")
            exit()

    print(data[-1] * A + B)