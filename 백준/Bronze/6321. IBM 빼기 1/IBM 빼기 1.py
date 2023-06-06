import sys

n = int(sys.stdin.readline())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    print(f"String #{_+1}")
    new_name = ""
    for ch in name:
        if ch == 'Z':
            new_name += 'A'
        else:
            new_name += chr(ord(ch) + 1)
    print(new_name)
    if _ != n-1:
        print()
