import sys

word = sys.stdin.readline().rstrip()
ans = 0
n = len(word)
pi = [0] * 5001

for i in range(n):
    k = 0
    for j in range(i + 1, n):
        while k > 0 and word[j] != word[i + k]:
            k = pi[k - 1]
        if word[j] == word[i + k]:
            k += 1
            if ans < k:
                ans = k
        pi[j - i] = k

print(ans)
