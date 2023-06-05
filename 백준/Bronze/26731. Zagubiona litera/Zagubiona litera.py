import sys

letters = sys.stdin.readline().rstrip()
total_ascii = sum(ord(ch) for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
missing_ascii = sum(ord(ch) for ch in letters)
missing_letter = chr(total_ascii - missing_ascii)
print(missing_letter)