import sys

n = int(sys.stdin.readline())

row = (n - 1) // 8 + 1
column = (n - 1) % 8 + 1

column_letter = chr(ord('a') + column - 1)

print(f"{column_letter}{row}")
