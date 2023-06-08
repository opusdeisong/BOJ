import sys

n = int(sys.stdin.readline())

unique_birthdays = set()

for _ in range(n):
    birthday = sys.stdin.readline().rstrip()

    unique_birthdays.add(birthday)

print(len(unique_birthdays))
