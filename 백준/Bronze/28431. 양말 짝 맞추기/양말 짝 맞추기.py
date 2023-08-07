import sys

arr = []

for _ in range(5):
    arr.append(int(sys.stdin.readline()))

ans = []

for i in range(10):
    if arr.count(i) % 2 == 1:
        print(i)
        break