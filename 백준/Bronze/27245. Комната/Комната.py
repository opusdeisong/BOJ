import sys

w = int(sys.stdin.readline())
l = int(sys.stdin.readline())
h = int(sys.stdin.readline())

smaller = min(w, l)
larger = max(w, l)

# Check the conditions
if smaller / h >= 2 and larger / smaller <= 2:
    print("good")
else:
    print("bad")
