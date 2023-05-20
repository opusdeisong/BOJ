import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
arr = [8, 9]
if a in arr and d in arr and b == c:
    print("ignore")
else:
    print("answer")