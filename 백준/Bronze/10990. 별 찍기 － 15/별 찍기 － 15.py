import sys


def print_star(n):
    for i in range(n):
        spaces_before = ' ' * (n - i - 1)
        spaces_in_between = ' ' * (2 * i - 1)
        if i == 0:
            print(spaces_before + '*')
        else:
            print(spaces_before + '*' + spaces_in_between + '*')

n = int(sys.stdin.readline())
print_star(n)
