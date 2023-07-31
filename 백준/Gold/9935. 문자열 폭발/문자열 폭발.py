import sys

a = sys.stdin.readline().rstrip()
b = list(sys.stdin.readline().rstrip())
temp = len(b)
arr = []
for i in a:
    arr.append(i)
    if i == b[-1] and arr[-temp:] == b:
        for _ in range(temp):
            arr.pop()

print(''.join(arr)) if arr else print("FRULA")