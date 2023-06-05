import sys

found = False
for i in range(5):
    if 'FBI' in sys.stdin.readline().rstrip():
        print(i + 1, end=' ')
        found = True
if not found:
    print("HE GOT AWAY!")
