import sys

word = input()
words = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = list(word)[:i]
        b = list(word)[i:j]
        c = list(word)[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        words.append(a + b + c)
words.sort()
for i in words[0]:
    print(i, end='')