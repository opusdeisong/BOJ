import sys

T = int(sys.stdin.readline())

char_mapping = {}

for _ in range(T):
    char, binary = sys.stdin.readline().split()
    char_mapping[binary] = char

runestone = input()

translated = ''
for i in range(0, len(runestone), 4):
    binary = runestone[i:i+4]
    if binary in char_mapping:
        translated += char_mapping[binary]
    else:
        translated += '?'

print(translated)
