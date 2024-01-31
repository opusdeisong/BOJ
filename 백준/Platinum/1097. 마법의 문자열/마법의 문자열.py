import itertools
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


def kmp(pattern, all_string, k):
    table = get_pi(pattern)
    count = -1
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i - 1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                count += 1
                i = table[i - 1]

    return count == k


n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
k = int(sys.stdin.readline())

answer = 0
permutations = itertools.permutations(words, n)
for perm in permutations:
    combined_string = ''.join(perm)
    if kmp(combined_string, combined_string + combined_string, k):
        answer += 1

print(answer)