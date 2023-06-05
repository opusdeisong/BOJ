import sys

def find_winner(s):
    A, B = 0, 0
    for i in range(0, len(s), 2):
        if s[i] == 'A':
            A += int(s[i + 1])
        else:
            B += int(s[i + 1])

        if max(A, B) >= 11 and abs(A - B) >= 2:
            return 'A' if A > B else 'B'
    return 'TIE'


s = sys.stdin.readline().rstrip()
print(find_winner(s))
