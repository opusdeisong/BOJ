N = int(input())
N = N ** 2
ans=0
A=0
B=-100
while True:
    if 0 <= A <= B:
        break
    ans += 1
    a = (1 - N) / (1 + N) * A + 2 * N / (1 + N) * B
    b = (N - 1) / (N + 1) * B + 2 / (N + 1) * A
    A = a; B = b
    if A < 0:
        ans += 1
        A *= -1
print(ans)