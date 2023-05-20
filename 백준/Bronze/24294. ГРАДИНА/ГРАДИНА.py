import sys

w1 = int(sys.stdin.readline())
h1 = int(sys.stdin.readline())
w2 = int(sys.stdin.readline())
h2 = int(sys.stdin.readline())

print(4 + 2 * max(w1, w2) + 2 * (h1 + h2))