import sys

hacker_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}

text = sys.stdin.readline().rstrip()

for original, replacement in hacker_map.items():
    text = text.replace(original, replacement)

print(text)