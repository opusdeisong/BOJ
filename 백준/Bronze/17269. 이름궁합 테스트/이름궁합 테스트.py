
N, M = map(int, input().split())
A, B = input().split()
alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
AB = ""
end = min(N, M)

for i in range(end):
    AB += A[i] + B[i]
AB += A[end:] + B[end:]

lst = [alp[ord(i) - ord('A')] for i in AB]

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        lst[j] += lst[j + 1]

print(f"{lst[0] % 10 * 10 + lst[1] % 10}%")