import sys

isbn_prefix = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
isbn_suffix = [int(sys.stdin.readline()) for _ in range(3)]
isbn = isbn_prefix + isbn_suffix

isbn_checksum = sum(val if i % 2 == 0 else val * 3 for i, val in enumerate(isbn))

print(f'The 1-3-sum is {isbn_checksum}')