import sys

arr = []
for i in range(2):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    arr.append(a * 3 + b * 2 + c)
if arr[0] == arr[1]:
    print("T")
elif arr[0] > arr[1]:
    print("A")
else:
    print("B")