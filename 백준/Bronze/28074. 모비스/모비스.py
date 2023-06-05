import sys


def can_form_mobis(s):
    for ch in 'MOBIS':
        if s.count(ch) == 0:
            return "NO"
    return "YES"

s = sys.stdin.readline().rstrip()
print(can_form_mobis(s))
