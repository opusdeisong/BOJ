import sys

while True:
    pattern = sys.stdin.readline().rstrip()

    if pattern == ".":
        break

    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    if len(pattern) % (len(pattern) - table[-1]):
        print(1)
    else:
        print(len(pattern) // (len(pattern) - table[-1]))
