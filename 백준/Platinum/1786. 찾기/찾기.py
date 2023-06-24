import sys

text = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

table = [0] * len(pattern)
j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
        j = table[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
        table[i] = j

j = 0
idx_ans = []
ans_cnt = 0
for i in range(len(text)):
    while j > 0 and text[i] != pattern[j]:
        j = table[j - 1]
    if text[i] == pattern[j]:
        if j == len(pattern) - 1:
            idx_ans.append(i - len(pattern) + 2)
            ans_cnt += 1
            j = table[j]
        else:
            j += 1

print(ans_cnt)
for w in idx_ans:
    print(w, end=" ")