import sys


def compute_fail_array(B):
    fail = [0] * len(B)
    j = 0
    for i in range(1, len(B)):
        while j > 0 and B[i] != B[j]:
            j = fail[j - 1]
        if B[i] == B[j]:
            j += 1
            fail[i] = j
    return fail

def string_matching(A, B):
    N = len(A)
    A = A + A
    N *= 2
    fail = compute_fail_array(B)
    ans = 0
    j = 0
    for i in range(N - 1):
        while j > 0 and A[i] != B[j]:
            j = fail[j - 1]
        if A[i] == B[j]:
            if j == len(B) - 1:
                ans += 1
                j = fail[j]
            else:
                j += 1
    return ans

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
print(string_matching(A, B))
