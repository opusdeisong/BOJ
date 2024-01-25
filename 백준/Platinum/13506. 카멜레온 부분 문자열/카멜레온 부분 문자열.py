import sys

def get_pi(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

S = sys.stdin.readline().rstrip()
pi = get_pi(S)
l = len(S)
M = pi[l - 1]

while M > 0:
    for i in range(1, l - 1):
        if pi[i] == M:
            print(S[:M])
            exit()
    M = pi[M - 1]
print(-1)