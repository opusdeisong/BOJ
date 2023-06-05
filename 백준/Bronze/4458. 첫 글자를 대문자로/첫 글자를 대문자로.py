import sys

N = int(sys.stdin.readline())
for _ in range(N):
    sentence = sys.stdin.readline().rstrip()
    print(sentence[0].upper() + sentence[1:])