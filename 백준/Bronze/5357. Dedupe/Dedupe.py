import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline().rstrip()

    deduped_string = string[0]

    for char in string[1:]:
        if char != deduped_string[-1]:
            deduped_string += char

    print(deduped_string)
