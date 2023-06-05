import sys

word = sys.stdin.readline()

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in word:
    if char in vowels:
        count += 1

print(count)
