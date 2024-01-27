import sys

t = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    S = sys.stdin.readline().rstrip()

    pi = [0] * len(S)
    for i in range(1, len(S)):
        j = pi[i - 1]
        while j > 0 and S[i] != S[j]:
            j = pi[j - 1]
        if S[i] == S[j]:
            j += 1
        pi[i] = j

    L = len(S)
    print(f"Test case #{t}")
    for i in range(1, L + 1):
        if i % (i - pi[i - 1]) == 0 and i // (i - pi[i - 1]) > 1:
            print(f"{i} {i // (i - pi[i - 1])}")
    print()
    t += 1