import sys

input_string = sys.stdin.readline().rstrip()

letter_counts = {}
for letter in input_string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

all_even = all(count % 2 == 0 for count in letter_counts.values())
all_odd = all(count % 2 == 1 for count in letter_counts.values())

if all_even:
    print(0)
elif all_odd:
    print(1)
else:
    print(2)
